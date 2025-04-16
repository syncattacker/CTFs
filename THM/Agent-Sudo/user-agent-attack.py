#!/usr/bin/python

import requests

matcher = b'\n<!DocType html>\n<html>\n<head>\n\t<title>Annoucement</title>\n</head>\n\n<body>\n<p>\n\tDear agents,\n\t<br><br>\n\tUse your own <b>codename</b> as user-agent to access the site.\n\t<br><br>\n\tFrom,<br>\n\tAgent R\n</p>\n</body>\n</html>\n'


header = { 'User-Agent' : '' }

fuzzwords = open("user-agent-fuzz.txt", "r")
agents = fuzzwords.readlines()

for agent in agents:
	header['User-Agent'] = agent.strip("\n")
	response = requests.get("http://10.10.21.125/", headers = header)
	if response.status_code == 200 and response.content == matcher:
		print("Blocked Response!")
	else:
		print(header['User-Agent'])
		print(response.text)

