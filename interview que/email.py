
import smtplib
import ssl
from email.mime.text import MIMEText

def send_email(sender_email, receiver_email, password, subject, body):
    """
    Sends a plain text email to a recipient.
    """

    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    smtp_server = "smtp.gmail.com"
    port = 587

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.send_message(message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example Usage: Replace with your actual email credentials and details
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@example.com"
password = "your_app_password"
subject = "Test Email from Python"
body = "This is a test email sent using a Python program."

send_email(sender_email, receiver_email, password, subject, body)