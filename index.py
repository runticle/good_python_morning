from twilio.rest import Client
from phone_nums import phone_numbers
from happy_messages import messages
import random

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = # get ya own
auth_token = # get ya own

client = Client(account_sid, auth_token)

def sendMessage(message, to_number):
    message = client.messages.create(
        body=message,
            from_= # my twilio num
            to=to_number
    )

def getRandom(from_list):
    return random.choice(from_list)


def runScript():
    # recipient = getRandom(phone_numbers)
    message = getRandom(messages)
    recipient = # my num
    sendMessage(message, recipient)


runScript()