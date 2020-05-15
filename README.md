# Good Python Morning!

I made a super simple script to send happy morning messages to some friends.

I used the Twilio API and set it up on AWS Lambda to send a message every morning at 9.30am.

It select a random phone number from an array of some peoples numbers, and selects a random message from an array of weird messages I found on the internet.

If the weather is more than 15°C forecast for the day, the message sent is instead a weather message with the temp and description. lol.

Easy as py!

# To use

Just clone the thing, set up a lambda function (using python 3.8) and add a `phone_nums` file with an array called `phone_numbers`.

Add your Twilio account as env variables

Jobs a goodun

Bye!

NB. It does require 3.7 and most macs have 2.7 installed by default so watch out
To upgrade follow steps here https://opensource.com/article/19/5/python-3-default-mac
