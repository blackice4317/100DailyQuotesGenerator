import datetime as dt
import random
from twilio.rest import Client
import os

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

now = dt.datetime.now()
hour = now.hour

if hour == 17:
    with open("100Quotes.txt", "r") as Quotes:
        content = Quotes.read().splitlines()

    quote = random.choice(content)
    message = client.messages.create(
        body=f"Today's Quote.\nQuote No {quote}",
        from_="+15854499684",
        to="+2348035760418",
    )

    print(message.status)
