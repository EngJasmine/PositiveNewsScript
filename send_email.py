
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib, ssl

def send_email(body):
    msg = MIMEMultipart()
    msg['From'] = "useremail@example.com"  # Replace with your email
    msg['To'] = "receiveremail@example.com"  # Replace with the recipient's email
    msg['Subject'] = "Today's Positive News"

    # Attach the body as plain text
    msg.attach(MIMEText(body, 'plain'))

    # Set up the server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login("reema5khamassi@gmail.com",
                     os.getenv("PASSWORD"))  # Replace with your email credentials
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

