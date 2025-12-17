import smtplib
from email.message import EmailMessage
from config import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD

def enviar_correo(destinatario, asunto, cuerpo):
    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = destinatario
    msg["Subject"] = asunto
    msg.set_content(cuerpo)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
