import smtplib
from email.mime.text import MIMEText
from config import settings

def send_message(to,subject,text):
    message=MIMEText(text,"plain")
    message['Subject']=subject
    message['From']="ИС регистрация"
    message['To']=to

    with smtplib.SMTP(settings.EMAIL_SMTP,settings.EMAIL_PORT) as server:
        server.starttls()
        server.login(settings.EMAIL_LOG,settings.EMAIL_PWD)
        server.sendmail(settings.EMAIL_LOG,to,message.as_string())