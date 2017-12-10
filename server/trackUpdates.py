from socketIO_client import SocketIO, LoggingNamespace
from pymongo import MongoClient
import sms
import os


def on_connect():
    print('connect')

def on_disconnect():
    print('disconnect')

def on_reconnect():
    print('reconnect')


class responseTracker:
    def __init__(self, to, phone):
        self.to = to
        self.phone = phone
    def notify(self, *args):
        notification = sms.Notification(twillo=[os.environ['TWILIO_ACCOUNT'],
            os.environ['TWILIO_SECRET'],
            os.environ['TWILIO_NUMBER']])
        message = args[0]['updated']['title']
        notification._sendSMS(self.phone, message)

if __name__ == "__main__":
    socketIO = SocketIO('localhost', 5000, LoggingNamespace)
    client = MongoClient()
    db = client['policeDB']
    reports = db.reportsToTrack
    while True:
        for onesToTrack in reports.find({}):
            to = onesToTrack['id']
            new = responseTracker(onesToTrack['id'], onesToTrack['phone'])
            socketIO.on(to, new.notify)
        socketIO.wait(seconds=30) # preform a refresh every 30 seconds.

