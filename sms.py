"""Before running...
Install selenium
sudo pip3 install selenium
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time,sys,os,platform
from config import username,password
import paths



#Returns the Path to appropriate ChromeDriver based on the type of system 
def find_system_driver():
	myOS = sys.platform
	#32bit or 64bit
	arch = platform.architecture()[0]

	if myOS.startswith('linux') and arch.startswith('32'):
		return '/ChromeDriver/Linux/32/'	
	elif myOS.startswith('linux') and arch.startswith('64'):
		return '/ChromeDriver/Linux/64/'
	elif myOS == 'darwin':
		return '/ChromeDriver/MacOS/'
	elif myOS.startswith('win') and arch.startswith('32'):
		return '\\ChromeDriver\\Windows\\32\\'
	elif myOS.startswith('win') and arch.startswith('64'):
		return '\\ChromeDriver\\Windows\\64\\'
	else:
		raise Exception('Unknown Operating System or Platform Architecture!')

def Set_Path_For_Chrome():
	pwd = os.path.abspath(os.getcwd())
	path_to_chrome_driver = pwd+find_system_driver()
	new_path = os.environ['PATH']+':'+path_to_chrome_driver
	os.environ['PATH'] = new_path
	#print(new_path)

def handle_popup(driver):
	print("There is a popup indeed...")
	driver.switch_to.window(driver.window_handles[-1])
	driver.close()
	driver.switch_to.window(driver.window_handles[0])

def login(driver):
	user_el = driver.find_element_by_id("username")	
	pass_el = driver.find_element_by_id("password")

	user_el.send_keys(username)
	pass_el.send_keys(password)

	login_btn = driver.find_element_by_css_selector(paths.login_btn_css)

	login_btn.click()
	
def send_msg(driver,to,msg):

	iframe_el = driver.find_element_by_xpath(xpath="//iframe[@id='by2Frame']")

	driver.switch_to.frame(frame_reference=iframe_el)

	sms_box_el = driver.find_element_by_class_name(paths.sms_box_class)

	to_el = sms_box_el.find_element_by_xpath("//input[@placeholder='Enter Mobile Number or Name']")
	to_el.send_keys(to)

	msg_el = sms_box_el.find_element_by_id(paths.msg_input_id)
	msg_el.send_keys(msg)

	send_now_btn = sms_box_el.find_element_by_xpath("//input[@id='btnsendsms']")
	send_now_btn.click()
	print("Send Now, button has been clicked...")

def load_profile():

	chrome_options = Options()
	chrome_options.add_argument("--headless")
	driver = webdriver.Chrome(chrome_options=chrome_options)
	return driver


def send(to,msg):

	#Urls..
	home_page = "http://www.160by2.com/"

	#Set the path to locate Chrome Driver for firefox..
	Set_Path_For_Chrome()

	driver = load_profile()

	driver.get(home_page)

	#Handle Popups...
	if len(driver.window_handles)>1:
		handle_popup(driver)
	else:
		print("No popups..")

	login(driver)
	
	#Wait for dashboard to load
	time.sleep(4)

	send_msg(driver,to,msg)
	
	#Wait for message to be sent
	time.sleep(5)
	
	#Exit chrome 
	driver.quit()
