import smtplib
from celery import Celery
from email.message import EmailMessage
from config import REDIS_HOST, REDIS_PORT, SMTP_PASSWORD, SMTP_USER

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('email_message', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')

def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['Subject'] = 'Уведомление о мероприятии'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username} присоединился к вашему мероприятию</h1>'
        '</div>',
        subtype='html'
    )
    return email


@celery.task
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email,to_addrs="sghsshsh03@gmail.com") 