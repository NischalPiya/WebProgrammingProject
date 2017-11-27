from twilio.rest import Client
from credentials import account_sid,auth_token,my_phone_number,twilio_phone_number
from Server import


def phone_sms():
    client = Client(account_sid, auth_token)

    message = client.messages.create(to=my_phone_number,from_=twilio_phone_number,body="Hey, Its a test!")
    print(message.sid)

phone_sms()