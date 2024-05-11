import smtplib
from email.mime.text import MIMEText
from config import settings

def send_email_message(to,subject,text):
    message=MIMEText(text,"html")
    message['Subject']=subject
    message['From']=settings.EMAIL_LOG
    message['To']=to
    try:
        with smtplib.SMTP_SSL(settings.EMAIL_SMTP,settings.EMAIL_PORT) as server:
            # server.starttls()
            server.login(settings.EMAIL_LOG,settings.EMAIL_PWD)
            server.sendmail(settings.EMAIL_LOG,to,message.as_string())
    except Exception as e:
        print(e)