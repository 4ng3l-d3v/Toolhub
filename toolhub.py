### Importing libraries. ###
import os, sys, time, webbrowser
from termcolor import colored

### Welcome... ###
os.system("clear")
print(colored("Welcome to toolhub!", "red"))
print()
print(colored("Toolhub is a programm that helps you to install popular hacking tools.\nI didn't create these instruments, i just found them for you!\n/Help command - for help i guess...\n", "yellow"))

def main():
	#  --- tools list --- 
	print("\n--- Tools list ---\n")
	print("SQL HACKING:")
	print(colored("[1] -- SQLMap (http://sqlmap.org)", 'magenta'))
	print("LOCALHOST PHISHING:")
	print(colored("[2] -- SocialFish (https://github.com/UndeadSec/SocialFish)", 'magenta'))
	print("PORT SCANNING:")
	print(colored("[3] -- Nmap (nmap.org) - Can be used already", 'green'))
	print("BETTER TERMINAL:")
	print(colored("[4] -- Iterm2 (https://iterm2.com/)", 'magenta'))


	installation = input(colored("Enter the tool's number >>> ", 'cyan'))

	if installation == "1":
		print("\nDownloading SQLMap...")
		time.sleep(1)
		os.system("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev")
		time.sleep(3)
	if installation == "2":
		print("\nDownloading SocialFish...")
		time.sleep(1)
		os.system("git clone https://github.com/UndeadSec/SocialFish.git")
		time.sleep(3)

	if installation == "3":
		nmap_usage = input("Target for scanning >>> ")
		os.system('nmap ' + nmap_usage)

	if installation == "4":
		print("Opening https://iterm2.com...")
		time.sleep(1)
		webbrowser.open_new("https://iterm2.com/")


		print(colored("\nClose toolhub?(y/n)", 'cyan'))
		close_or_continue = input(">>> ")

		if close_or_continue == "y": # if user chose yes(close the window)
			print('Quiting...')
			time.sleep(2)
			os.system('exit()')

		if close_or_continue == "n": # if user chose no(to still use the programm)
			start()


		


### Working with programm. ### 

def start():
	command = input("Thub >>> ")
	if command == "/help":
		print(colored("\n/start - Start the programm\n/help - Help(commands list)\n/exit - Exit\n/iterm - macOS terminal replacement(better use toolhub with it)\nOther functions are in progress... ", "cyan"))
		start()

	if command == "help":
		print(colored('\nHeeey, you forgot about "/"\n', 'red'))
		start()

	if command == "/start":
		main() #Calling the main function.

	if command == "/exit":
		os.system('exit()')

	if command == "/iterm":
		webbrowser.open_new("https://iterm2.com/")
		time.sleep(1)
		start()





    
	
start()






