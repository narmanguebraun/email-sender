import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path #pathlib instead of os.path, to access html file


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = '<from_name>'
email['to'] = '<to_email>'
email['subject'] = 'See you in Paris?'

# email.set_content('28 boulevard des Capucines. July 07 at 19:30.')

email.set_content(html.substitute({'address': '28 boulevard des Capucines', 'day': 'July 07', 'hour': '19:30'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('<from_email>', '<from_email_password>')
  smtp.send_message(email)
  print('it works')
