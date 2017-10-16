import message
import otp
import sms

otp_size = 5
target = message.to

def main():
	new_otp = otp.generate(otp_size)
	
	msg = "Your {0} digit OTP is as follows: {1}, it expires in 2 minutes!".format(otp_size,new_otp)
	
	sms.send(target,msg)

if __name__=='__main__':
	main()