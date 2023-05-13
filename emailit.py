import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Beállítjuk az SMTP szervert és portot
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Létrehozunk egy MIMEMultipart objektumot
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Hozzáadjuk az üzenetet a MIMEMultipart objektumhoz
    msg.attach(MIMEText(message, 'plain'))

    # SMTP kapcsolat létrehozása és bejelentkezés
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Email küldése
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Kijelentkezés és kapcsolat bezárása
    server.quit()

# Példa használat
sender_email = 'your_email@gmail.com'
sender_password = 'your_password'
recipient_email = 'recipient_email@example.com'
subject = 'Teszt üzenet'
message = 'Ez egy teszt üzenet.'

#send_email(sender_email, sender_password, recipient_email, subject, message)
