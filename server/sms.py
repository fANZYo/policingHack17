import os
import sys

from twilio.rest import Client

class Notification:
    def __init__(self, twillo=None):
        if twillo != None:
            account = twillo[0]
            token = twillo[1]
            self.fromNumber = twillo[2]
            self.client = Client(account, token)
    def _sendSMS(self, to, rawMessage):
        actualMessage = rawMessage[:140]
        if len(actualMessage) == 140:
            actualMessage = actualMessage[:137]+'...'
        if len(actualMessage) == 0:
            return
        message = self.client.messages.create(to=to, from_=self.fromNumber,
                body=actualMessage)

if __name__ == "__main__":
    notification = Notification(twillo=[os.environ['TWILIO_ACCOUNT'],
        os.environ['TWILIO_SECRET'],
        os.environ['TWILIO_NUMBER']])
    notification._sendSMS("<BLANKED>","omg"*100)
