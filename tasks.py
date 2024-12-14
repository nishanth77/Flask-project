import os
import requests
from dotenv import load_dotenv

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")

def send_simple_message(to, subject, body):
    # domain = os.getenv("MAILGUN_DOMAIN")
    return requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN}/messages",
        auth = ("api", os.getenv("MAILGUN_API_KEY")),
        data = { "from": "Nishanth Thangaraj <mailgun@{DOMAIN}}>",
                "to": to,
                "subject": subject,
                "text": body
        })

def send_user_registration_email(email,username):
    return send_simple_message(to=email, "Successfully signed Up", f"Hi {username}! You have successfully signed up")