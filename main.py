import sys
import otp
import sms

#Lenght of OTP (digits)
otp_size = 5

#The target mobile number, passed as a commandline argument...
target = sys.argv[1]

def main():
	
	print("Generating OTP, Please wait......")

	#Get new otp
	new_otp = otp.generate(otp_size)
	
	#Craft the message to be sent
	msg = "Your {0} digit OTP is as follows: {1}, it expires in 2 minutes!".format(otp_size,new_otp)
	
	#Send the message
	sms.send(target,msg)

	input_otp = input("Enter the OTP Received: ")

	if input_otp==new_otp:
		print("\n************Access Granted************\n")
	else:
		print("Error, Wrong OTP entered!!")
		print("\n------------Access Denied-------------\n")


if __name__=='__main__':
	main()