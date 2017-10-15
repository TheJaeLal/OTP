"""Before running...
Install selenium
sudo pip3 install selenium
"""
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
import time,sys,os,platform

#Take email and password from command line
email = sys.argv[1]
password = sys.argv[2]


#Returns the Path to appropriate GeckoDriver based on the type of system 
def find_system_driver():
	myOS = sys.platform
	#32bit or 64bit
	arch = platform.architecture()[0]

	if myOS.startswith('linux') and arch.startswith('32'):
		return '/GeckoDriver/Linux/32/'	
	elif myOS.startswith('linux') and arch.startswith('64'):
		return '/GeckoDriver/Linux/64/'
	elif myOS == 'darwin':
		return '/GeckoDriver/MacOS/'
	elif myOS.startswith('win') and arch.startswith('32'):
		return '\\GeckoDriver\\Windows\\32\\'
	elif myOS.startswith('win') and arch.startswith('64'):
		return '\\GeckoDriver\\Windows\\64\\'
	else:
		raise Exception('Unknown Operating System or Platform Architecture!')

def Set_Path_For_Firefox():
	pwd = os.environ['PWD']
	path_to_gecko = pwd+find_system_driver()
	new_path = os.environ['PATH']+':'+path_to_gecko
	os.environ['PATH'] = new_path

def login(driver):
	pass


def main():

	#Urls..
	home_page = "http://www.160by2.com/Main.action?id="

	#Set the path to locate Gecko Driver for firefox..
	Set_Path_For_Firefox()

	driver = webdriver.Firefox()

	driver.get(home_page)

	login(driver)


if __name__== "__main__":
	main()