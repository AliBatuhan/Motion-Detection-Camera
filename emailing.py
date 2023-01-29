import smtplib
import os
from email.message import EmailMessage
import imghdr

sender = os.getenv("USER001")
password = os.getenv("PASSWORD001")
receiver = os.getenv("USER001")

def send_email(image_path):
    print("send function  started")
    email_message = EmailMessage()
    email_message["Subject"] = "Some one is there! "
    email_message.set_content("Hey smo is here look! ")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype = "image", subtype =imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, receiver, email_message.as_string())
    gmail.quit()
    print("send function  ended")

if __name__ == "__main__":
    send_email(image_path="images/5.png")