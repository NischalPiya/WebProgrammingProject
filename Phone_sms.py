from twilio.rest import Client
from Reminders import r
import os
import time
start_time=time.time()

account_ssid= os.environ['ACCOUNT_SSID']
auth_token=os.environ['ACCOUNT_TOKEN']
my_phone_number=os.environ['MY_PHONE_NUMBER']
twilio_phone_number=os.environ['TWILIO_PHONE_NUMBER']


def phone_sms():
    client = Client(account_ssid, auth_token)
    message = client.messages.create(to=my_phone_number,from_=twilio_phone_number,body="You have "+str(r.list_reminders()).strip('[]'))
    print(message.sid)




