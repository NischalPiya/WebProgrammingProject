from twilio.rest import Client
from credentials import account_ssid,auth_token,my_phone_number,twilio_phone_number
from Reminders import r
from Server import get_due_date

import os
import time
start_time=time.time()


while True:
    def phone_sms():


        client = Client(account_ssid, auth_token)

        message = client.messages.create(to=my_phone_number,from_=twilio_phone_number,body="You have "+str(r.list_reminders()).strip('[]'))
        print(message.sid)



    def phone_added_reminder_sms():

        client = Client(account_ssid, auth_token)

        message = client.messages.create(to=my_phone_number,from_=twilio_phone_number,body="You have "+str(r.new_canvas_reminder('5522','25628')).strip('[]'))
        print(message.sid)

    def phone_delete_reminder_sms():





    phone_added_reminder_sms()

    time.sleep(10)


