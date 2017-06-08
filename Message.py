import datetime


class Message:
    def __init__(self, channel, chatter, message):
        self.chatter = chatter
        self.message = message
        self.channel = channel
        self.time_received = datetime.datetime.now()


def make_message(channel, chatter, message):
    message = Message(channel, chatter, message)
    print("[%s] %-*s - %-*s: %s" % (message.time_received, 30, message.chatter, 30, message.channel, message.message))
    return message