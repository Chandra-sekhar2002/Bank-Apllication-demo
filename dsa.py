#SENDERMAIL = "bellanachandu2002@gmail.com"
#AILPASS = "8099134335"
import smtplib

SENDERMAIL = "21w91a0414@mriet.ac.in"
MAILPASS = "7995894097"

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(SENDERMAIL, MAILPASS)
    print("Login successful!")
    server.quit()
except Exception as e:
    print(f"Error: {e}")
