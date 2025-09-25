# email_utils.py
import aiosmtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

async def send_otp_email(recipient: str, otp: str, purpose: str):
    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = recipient
    msg["Subject"] = f"Your OTP for {purpose}"

    msg.set_content(f"Your OTP for {purpose} is: {otp}. It will expire in 10 minutes.")

    await aiosmtplib.send(
        msg,                
        hostname=SMTP_HOST,
        port=SMTP_PORT,
        username=SMTP_USER,
        password=SMTP_PASS,
        start_tls=True,
    )

