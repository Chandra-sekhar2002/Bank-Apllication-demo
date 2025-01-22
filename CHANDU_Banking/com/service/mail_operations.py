import time

import smtplib
from random import randint
from CHANDU_Banking.com.service.constants import *
from dsa import server

otp_data={}
# function that generates random number
def otp_gen():
    otp = randint(100000, 999999)
    return otp

# function that sends mail and verifies OTP
def mailOtpVerification(email):
    try:
        # senderMail = SENDERMAIL
        # password = MAILPASS
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(SENDERMAIL, MAILPASS)
        otp = otp_gen()
        timestamp=time.time()
        otp_data[email] = {"otp": otp, "timestamp": timestamp}
        message = f"Welcome to CHANDU Bank, Trust Above All.\n\nYour OTP is: {otp}\n\nThis OTP is valid for 5 minutes."
        server.sendmail(SENDERMAIL, email,message)
        print("otp sent to: " + email+" valid only for 5min")
        server.quit()
        print()
        user_otp = int(input("please Enter OTP to continue: "))

        if valid_otp(email, user_otp):
            print("OTP Verified!")
            return True
        else:
            print("OTP Verification Failed!")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False
def valid_otp(email,user_otp):
    current_time = time.time()  # Get current time in seconds
    if email in otp_data:
        generated_otp = otp_data[email]["otp"]
        otp_timestamp = otp_data[email]["timestamp"]

        # Check if the OTP matches
        if user_otp == generated_otp:
            # Check if the OTP is within the valid time limit (5 minutes = 300 seconds)
            if current_time - otp_timestamp <= 300:
                return True
            else:
                print("OTP has expired!")
                return False
        else:
            print("Invalid OTP!")
            return False
    else:
        print("No OTP found for this email!")
        return False
#=>email = input("Enter email:")
#=>mailOtpVerification(email)


def statement_sent_to(email,statement):
    #function to send transaction history to user_email
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(SENDERMAIL, MAILPASS)
    server.sendmail(SENDERMAIL,email,statement)
    print("statement sent to "+email)
    server.quit()
    return True

