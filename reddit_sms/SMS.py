import smtplib
import cred
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send(message):
    to_number = cred.keyring.get_password('phone_number', 'phone_num')
    auth = (cred.keyring.get_password('gmail_user', 'gmail_username'), cred.keyring.get_password('gmail_pass', 'gmail_pass'))

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(auth[0], auth[1])

    # Use the MIME module to structure your message.
    msg = MIMEMultipart()
    msg['From'] = auth[0]
    msg['To'] = to_number
    body = message
    # Attach the body
    msg.attach(MIMEText(body, 'plain'))

    sms = msg.as_string()

    server.sendmail(auth[0], to_number, sms)

    # Quit the server
    server.quit()
