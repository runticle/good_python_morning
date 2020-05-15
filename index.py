import base64
import json
import os
import urllib
import random
from dotenv import load_dotenv
from urllib import request, parse
from phone_nums import phone_numbers
from happy_messages import messages

load_dotenv()

TWILIO_SMS_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
MY_NUMBER = os.environ.get('MY_NUMBER')

def lambda_handler(event, context):
    if not TWILIO_ACCOUNT_SID:
        print("Unable to access Twilio Account SID.")
    elif not TWILIO_AUTH_TOKEN:
        print("Unable to access Twilio Auth Token.")

    to_number=getRandom(phone_numbers)
    from_number='+447380336714'
    body=getRandom(messages)
    
    print("Attempting to send... ")
    print(body)
    print("to...")
    print(to_number)
    
    # send to me if test
    # if(event['test']):
    #     to_number = MY_NUMBER

    # insert Twilio Account SID into the REST API URL
    populated_url = TWILIO_SMS_URL.format(TWILIO_ACCOUNT_SID)
    post_params = {"To": to_number, "From": from_number, "Body": body}

    # encode the parameters for Python's urllib
    data = parse.urlencode(post_params).encode()
    req = request.Request(populated_url)

    # add authentication header to request based on Account SID + Auth Token
    authentication = "{}:{}".format(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    base64string = base64.b64encode(authentication.encode('utf-8'))
    req.add_header("Authorization", "Basic %s" % base64string.decode('ascii'))

    try:
        # perform HTTP POST request
        with request.urlopen(req, data) as f:
            print("Twilio returned {}".format(str(f.read().decode('utf-8'))))
    except Exception as e:
        print('Error from Twilio ->') 
        print (e)
        return e

    print("SMS sent successfully!")

def getRandom(from_list):
    return random.choice(from_list)


lambda_handler({"test": True}, 1)