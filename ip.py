try:
	import socket
	import os
	import time
	
	from colorama import Fore, Style, Back
	
except ImportError as e:
	print("Import error brader " + str(e))
	
BACKYELLOW = Back.YELLOW
RESET = Style.RESET_ALL

def banner():
	print(Fore.RED+f"""
       ╦┌─┐
       ║├─┘
       ╩┴   {BACKYELLOW}Domain To IP
	{RESET}""")
	
def GetIP(site):
	site = i.strip()
	try:
		if 'http://' not in site:
			get1 = socket.gethostbyname(site)
			print(Fore.GREEN+f"IP :{RESET}", get1)
			open("result.txt", 'a').write(get1 + "\n")
		
		elif 'http://' or 'https://' in site:
			rep = site.replace('http://', '').replace('https://', '').replace('/', '')
			get2 = socket.gethostbyname(rep)
			print(Fore.GREEN+f"IP :{RESET}", get2)
			open("result.txt", 'a').write(get2 + "\n")
			
	except:
		pass

banner()
list = str(input("Domain List -> "))

try:
	with open(list) as f:
		for i in f:
			GetIP(i)
			
except IOError as err:
	print("Error Brader " + str(err))
