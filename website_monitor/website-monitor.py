import requests
import smtplib
import os
# from dotenv import load_dotenv
# load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')


def send_notification(email_content):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        #smtp.sendmail(sender, receiver, message)
        email_content = f"Subject:WEB MONITOR ALERT\n{email_content}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, email_content)


try:
    r = requests.get(
        'http://ec2-18-184-246-158.eu-central-1.compute.amazonaws.com:8080/')
    if r.status_code == 200:
        print("Website is up!")
    else:
        print("Website is down!")
        # send email
        message = "Website is down!"
        send_notification(message)
except Exception as e:
    print(f"Connection error: {e}")
    message = "Connection error!"
    send_notification(message)
