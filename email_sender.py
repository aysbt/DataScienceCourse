import smtplib
from email.message import EmailMessage
from string import  Template
from pathlib import Path

html = Template(Path('index.html').read_text())


#gamil for sending email
your_email = 'ccovet.game@gmail.com'
your_password = 'mwxpylcmeoenqkwd'

email = EmailMessage()

email['from'] = 'Ayse Bat'
email['to'] = 'ayse_2998@hotmail.com'
email['subject'] = 'You won 1,000,000 dollors'
email.set_content(html.substitute({'name':'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login(your_email, your_password)
    smtp.send_message(email)
    print('All good boss!!')





