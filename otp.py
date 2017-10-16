from random import randint

def generate(size):
	otp_length = size
	#Generte a 5 digit otp
	otp_digits  = [str(randint(0,9)) for _ in range(otp_length)]
	otp = "".join(otp_digits)
	return otp
