import celery, smtplib, sqlalchemy
from email.mime.text import MIMEText
from session import connect

celery = celery.Celery('tasks', broker='redis://localhost:6379', broker_connection_retry_on_startup=True)
login = 'login@ya.ru'
password = 'Parol'

@celery.task
def to_send(mail):
    msg = MIMEText('\n'.join(str(*a) for a in connect.session.execute(sqlalchemy.text('SELECT "Name" FROM sellers'))))
    msg['From'] = login
    msg['To'] = mail
    msg['Subject'] = 'Statistic'
    with smtplib.SMTP_SSL('smtp.yandex.com', 465) as smtp:
        smtp.ehlo()
        smtp.login(login, password)
        smtp.send_message(msg)
