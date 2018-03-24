import sys,os
from twilio.rest import Client

sid = 'ACf6c992110c5daf3e736e28e9d5e61d7f'
token = 'fa1d502e45bef0d61c9bfce322cdc9ae'
client = Client(sid, token)

#thas me number
testnumber = '+18622203434'
#emergency
emergency = '911'
#number from twilio
fromPhone = '+14697784122'

#message is the body of the text
def sendMessage(message):
    client.messages.create(body = message, to = testnumber,
                           from_ = fromPhone)

def genMessage():
    pass