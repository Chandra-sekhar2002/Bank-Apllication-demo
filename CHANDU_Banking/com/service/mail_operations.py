import time

import smtplib
from random import randint
from CHANDU_Banking.com.service.constants import *
# function that generates random number
def otp_gen():
    otp = randint(100000, 999999)
    return otp


# function that sends mail and verifies OTP
def mailOtpVerification(email):


    # senderMail = SENDERMAIL
    # password = MAILPASS
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(SENDERMAIL, MAILPASS)

    otp = otp_gen()
    message = f"Welcome to FLM Bank, Trust Above All.\n\nYour OTP is: {otp}\n\nThis OTP is valid for 5 minutes."
    server.sendmail(SENDERMAIL, email,message)
    print("otp sent to: " + email)
    server.quit()
    print()
    user_otp = int(input("please Enter OTP to continue: "))

    if user_otp == otp:
        # print("OTP Verified")
        return True
    else:
        # print("OTP Not Verified")
        return False



# email = input("Enter email:")
#mailOtpVerification('gourusaikumar789@gmail.com')
