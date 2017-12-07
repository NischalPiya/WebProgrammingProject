from twilio.rest import Client
from credentials import account_ssid,auth_token,my_phone_number,twilio_phone_number
from Reminders import r
import time
start_time=time.time()


def phone_sms():
    client = Client(account_ssid, auth_token)
    message = client.messages.create(to=my_phone_number,from_=twilio_phone_number,body="You have "+str(r.list_reminders()).strip('[]'))
    print(message.sid)



