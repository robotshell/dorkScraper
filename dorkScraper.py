#!/usr/bin/env python

# Robot Scraper
#
# ORHOund is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Knock is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Knock. If not, see <http://www.gnu.org/licenses/>.

# Standard Python libraries
import sys
import requests
from bs4 import BeautifulSoup

class colors:
    HEADER = '\033[1;35m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKCYANL = '\033[1;36m'
    OKGREEN = '\033[92m'
    OKGREENL = '\033[1;32m' 
    OKREDL = '\033[1;31m' 
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner():
	print(colors.HEADER  + """
 ____             _     ____                                 
|  _ \  ___  _ __| | __/ ___|  ___ _ __ __ _ _ __   ___ _ __ 
| | | |/ _ \| '__| |/ /\___ \ / __| '__/ _` | '_ \ / _ \ '__|
| |_| | (_) | |  |   <  ___) | (__| | | (_| | |_) |  __/ |   
|____/ \___/|_|  |_|\_\|____/ \___|_|  \__,_| .__/ \___|_|   
                                            |_|                                                                   
""" + colors.ENDC)
	print(colors.OKGREENL + "DorkScraper v.1.0 - Open Source Project\n" + "Author: Robotshell\n" + "Github: https://github.com/robotshell\n" + colors.ENDC)

#CORE FUNCTION
def getRobots(domain,enable_save):

	print (colors.OKCYAN + "Starting RobotScraper to recollect directories and pages from " + colors.WARNING + "robots.txt " + colors.OKCYAN + "in " + colors.FAIL + domain + colors.ENDC)
	print (colors.OKCYAN + "[+] Checking if the" + colors.WARNING + " robots.txt " + colors.OKCYAN + "file exists" + colors.ENDC)

	r = requests.get("https://" + domain + "/robots.txt")

	if r.status_code == 200:
		print (colors.OKCYAN + "[✓] File" + colors.WARNING + " robots.txt " + colors.OKCYAN + "exists:" + colors.ENDC)
		print()
		soup = BeautifulSoup(r.text, 'html.parser')

		with open("response.txt", "w") as file:
    			file.write(str(soup))
		print (soup)

		file = open("response.txt", "rt")

		for line in file:
			a = 0
				
			if "Allow:" in line:
				directory = line.replace('Allow: ', '')
				a = 1

			if a == 0:
				directory = line.replace('Disallow: ', '')


			if directory[0] == '/':
	
				newDomain = "https://" + domain + directory
				r2 = requests.get(newDomain)
				
				print (colors.OKCYAN + "[+] Checking " + colors.WARNING + newDomain + colors.ENDC, end = '')

				if r2.status_code == 200:
					
					print (colors.OKGREEN + "[✓] Obtained a " + colors.WARNING + "200 OK " + colors.OKGREEN +  "success status response code in directory: " + colors.WARNING + directory + colors.ENDC)

				elif r2.status_code == 302:
					print (colors.OKGREEN + "[✓] Obtained a " + colors.WARNING + "302 Found redirect " + colors.OKGREEN +  "status response code in directory: " + colors.WARNING + directory + colors.ENDC)
				
				else:
					print (colors.FAIL + "[✓] Obtained a " + colors.WARNING + str(r2.status_code) + colors.FAIL +  " status response code in directory: " + colors.WARNING + directory + colors.ENDC)

		file.close()

     	
#MAIN FUNCTION
def main():
	banner()
	enable_save=0 
	
	if len(sys.argv) == 1:
		print (colors.FAIL + "ERROR: No domain or parameters found" + colors.ENDC)
	else:
		arg=sys.argv[1]
		if arg == "-h" or arg == "--help" :
			print (colors.BOLD + "HELP SECTION:" + colors.ENDC)
			print ("Usage:" + colors.OKCYAN + "\trobotscraper.py domain.com" + colors.ENDC)
			print ("-h,--help" + colors.OKCYAN + "\tThis help" + colors.ENDC)
			print ("-v,--version" + colors.OKCYAN + "\tShow version" + colors.ENDC)
			print ("-s,--save" + colors.OKCYAN + "\tEnable save output in .txt file" + colors.ENDC)
		elif arg == "-v" or arg == "--version":
			print ("RobotScraper v.1.0")
		elif arg == "-s" or arg == "--save":
			enable_save=1
			getRobots(arg,enable_save) 
		else:
			getRobots(arg,enable_save)
	
main()