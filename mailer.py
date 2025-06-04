import smtplib
from email.message import EmailMessage
import config
import os

def send_email(subject, body, to, attachment_path):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = config.EMAIL_FROM
    msg['To'] = to
    msg.set_content(body)

    with open(attachment_path, 'rb') as f:
        msg.add_attachment(f.read(), filename=os.path.basename(attachment_path),
                           maintype='application', subtype='octet-stream')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(config.EMAIL_FROM, config.EMAIL_PASSWORD)
        smtp.send_message(msg)
