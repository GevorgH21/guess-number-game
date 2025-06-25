import smtplib
import os
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content(f"GitHub Actions Job finished with status: {os.environ['JOB_STATUS']}")
msg["Subject"] = "CI/CD Status Notification"
msg["From"] = os.environ["GMAIL_USER"]
msg["To"] = os.environ["GMAIL_USER"]

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(os.environ["GMAIL_USER"], os.environ["GMAIL_PASS"])
    smtp.send_message(msg)

