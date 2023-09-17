import os
import base64
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

decode_env_variable = lambda value : \
        base64.b64decode(os.getenv(value)).decode('UTF-8')

def send_mail(send_from, send_to, subject, text, files=None,
              server="127.0.0.1"):
    assert isinstance(send_to, list)

    if os.getenv('SMTP_AUTH') == None:
        print('SMTP_AUTH environment variable is required')
        return

    smtp_auth_path = decode_env_variable('SMTP_AUTH')

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg['Content-Type'] = 'text/html; charset="UTF-8"'

    msg.attach(MIMEText(text, 'html'))

    for f in files or []:
        with open(f, "rb") as file:
            part = MIMEApplication(
                file.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    smtp = smtplib.SMTP(server, 587)
    smtp.starttls()
    smtp.login(send_from, smtp_auth_path)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
