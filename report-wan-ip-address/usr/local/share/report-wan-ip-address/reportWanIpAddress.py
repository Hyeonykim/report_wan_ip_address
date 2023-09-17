#!/usr/bin/env python3

import os
import sys
import base64
from sendEmail import send_mail
import requests

decode_env_variable = lambda value : \
        base64.b64decode(os.getenv(value)).decode('UTF-8')

def check_environment_variable():
    required_environment_variable = [
            'SMTP_SERVER',
            'SMTP_AUTH',
            'USER_EMAIL',
            'IP_INFO_URL'
        ]

    is_invalid = False
    for environment_variable in required_environment_variable:
        if os.getenv(environment_variable) == None:
            print(environment_variable + ' is required')
            is_invalid = True

    return is_invalid

if check_environment_variable() == True:
    sys.exit(0)

url = decode_env_variable('IP_INFO_URL')
response = requests.get(url)

ip_address = response.text

sender = decode_env_variable('USER_EMAIL')
smtp_server = decode_env_variable('SMTP_SERVER')
email_title = 'WAN IP Address'
send_mail(sender, [sender], email_title, ip_address, None, smtp_server)
