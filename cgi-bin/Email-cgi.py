#!/usr/bin/python3

import cgi
import smtplib

print("Content-text: text/html")
print()

def send_email(sender_email, sender_password, receiver_email, subject, body):
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 465

        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, sender_password)

        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, receiver_email, message)

        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print("Error sending email:", e)

# Example usage:
sender_email = 'mrroot0731@gmail.com'
sender_password = 'novdantblgdlzslc'

receiver = cgi.FieldStorage()
receiver_email = receiver.getvalue("r")
print(receiver_email)

mysubject = cgi.FieldStorage()
subject = mysubject.getvalue("s")
print(subject)

mybody = cgi.FieldStorage()
body = mybody.getvalue("b")
print(body)

send_email(sender_email, sender_password, receiver_email, subject, body)