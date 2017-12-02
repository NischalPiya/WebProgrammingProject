from twilio.rest import Client
from credentials import account_sid,auth_token,my_phone_number,twilio_phone_number
from Server import list_assignment
import os

import time
start_time=time.time()

acc_id=os.environ['account_ssid']
token=os.environ['auth_token']
phone_no=os.environ['my_phone_number']
twilio_no=os.environ['twilio_phone_number']

while True:
    def phone_sms():
        client = Client(acc_id, token)

        message = client.messages.create(to=phone_no,from_=twilio_no,body=list_assignment('5522'))
        print(message.sid)

    phone_sms()
    time.sleep(5.0)
