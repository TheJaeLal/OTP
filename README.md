# OTP
One Time Password (OTP) Verification System, that generates OTP and sends it via SMS to the specified mobile number, using [160by2](http://160by2.com/) sms-gateway as a backend.

Before Usage:

* Register on [160by2.com](http://160by2.com/), and get username(mobile-no) & password.

* Install selenium for python
  ```shell
  pip3 install selenium
  ```
* Download this repository

* Create a file name config.py inside the downloaded folder and enter your 160by2 username(mobile-no) & password
  ```python
  username = "923456781"
  password = "yourpassword"
  ```


Usage:

Execute Main.py file in the folder, by passing the mobile-no to which you want to send the otp as commandline argument
eg.
```shell
python main.py 923456782
```
The above command will send a 5-digit OTP to "923456782"




