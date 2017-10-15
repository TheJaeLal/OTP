"""Before running...
Install selenium
sudo pip3 install selenium
"""
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
import time,sys,os,platform
from config import username,password
import message
import paths

#Take email and password from command line
#email = sys.argv[1]
#password = sys.argv[2]


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
	pwd = os.path.abspath(os.getcwd())
	path_to_gecko = pwd+find_system_driver()
	new_path = os.environ['PATH']+':'+path_to_gecko
	os.environ['PATH'] = new_path
	#print(new_path)

def login(driver):
	user_el = driver.find_element_by_id("username")	
	pass_el = driver.find_element_by_id("password")

	user_el.send_keys(username)
	pass_el.send_keys(password)

	login_btn = driver.find_element_by_css_selector(paths.login_btn_css)

	login_btn.click()
	
def send_msg(driver,to,msg):
	to_el = driver.find_element_by_class_name(paths.mobile_no_input_ptag_class).find_element_by_xpath("//input")
	to_el.send_keys(to)

	msg_el = driver.find_element_by_id(msg_input_id)
	msg_el.send_keys(msg)

	send_now_btn = driver.find_element_by_id(paths.send_now_btn_id)
	send_now_btn.click()

def main():

	#Urls..
	home_page = "http://www.160by2.com/"

	#Set the path to locate Gecko Driver for firefox..
	Set_Path_For_Firefox()

	driver = webdriver.Firefox()

	driver.get(home_page)

	if len(driver.window_handles)>1:
		print("There is a popup indeed...")
		driver.switch_to.window(driver.window_handles[-1])
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
	else:
		print("No popups..")

	login(driver)
	msg = "working"
	to=username

	time.sleep(2)
	
	send_msg(driver,message.to,message.msg)

if __name__== "__main__":
	main()
