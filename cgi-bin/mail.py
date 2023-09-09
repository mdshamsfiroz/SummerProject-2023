#!/usr/bin/python

import cgi
import smtplib

print("Content-type: text/html\n\n")
print("<html>")
print("<head>")
print("<title>Email Status</title>")
print("</head>")
print("<body>")

form = cgi.FieldStorage()

# Retrieve form data
sender_email = form.getvalue("sender_email")
sender_password = form.getvalue("sender_password")
recipient_email = form.getvalue("recipient_email")
message = form.getvalue("message")

try:
    # Establish a connection to the Gmail SMTP server on port 587
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # Start a TLS (Transport Layer Security) encrypted connection
    server.starttls()

    # Login to the sender's Gmail account using the provided credentials
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, message)

    # Close the connection to the server
    server.quit()

    print("<p>Email sent successfully!</p>")
except Exception as e:
    print("<p>Error sending email: {}</p>".format(str(e)))

print("</body>")
print("</html>")