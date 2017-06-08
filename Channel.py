import threading
import random
import socket
from Message import make_message

server = 'irc.chat.twitch.tv'
nick = 'justinfan' + str(random.randint(892312, 1289798))
port = 80
message_list = []
BOT_LIST = ["neffyrobot", "gspbot", "tuckusruckusbot", "missychatbot", "6seven8_bot", "spindigbot", "jenningsbot", "lasskeepobot", "jogabot", "og_walkbot", "cinbot", "clickerheroesbot", "xnoobbot", "drunkafbot", "zmcbeastbot", "lucidfoxxbot", "moobot", "hnlbot", "scamazbot", "revobot", "vaneiobot", "korgek_bot", "gorobot", "toez_bot", "flpbot", "priestbot", "xanbot", "drangrybot", "phantombot", "coebot", "wizebot", "branebot", "vivbot", "revlobot", "ankhbot", "deepbot", "nightbot", "ohbot", "koalabot", "quorrabot"]


class Channel(threading.Thread):
    def __init__(self, thread_id, name, channels):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.streamers = channels
        self.irc = setup_connection(self.streamers, self.thread_id, self.name)

    def run(self):
        handle_messages(self.irc, self.thread_id, self.name)
        print("Channel thread ending: %s - %s" % (self.thread_id, self.name))


def setup_connection(channels, thread_id, name):
    irc = socket.socket()
    irc.connect((server, port))
    irc.send(bytes("NICK %s\r\n" % nick, "UTF-8"))
    for channel in channels:
        irc.send(bytes("JOIN #%s\r\n" % channel, "UTF-8"))
    return irc


def handle_messages(irc):
    reader = ""
    while 1:
        try:
            reader = reader + irc.recv(2048).decode("UTF-8")
            newmsg = str.split(reader, "\n")
            reader = newmsg.pop()
            for line in newmsg:
                line = str.strip(line)
                line = str.split(line)
                if line[0] == "PING":
                    irc.send(bytes("PONG %s\r\n" % line[1], "UTF-8"))
                if line[1] == "PRIVMSG" and line[0].split("!")[0].lstrip(":") not in BOT_LIST:
                    size = len(line)
                    i = 3
                    message = ""
                    while i < size:
                        message += line[i] + " "
                        i = i + 1
                    # ######## SPLIT TWITCH MESSAGE IRC LAYOUT ##########
                    #  line[0] = :[name]![name]![name].tmi.twitch.tv    #
                    #  line[1] = IRC Message Type (PING, PRIVMSG, etc.) #
                    #  line[2] = Channel name                           #
                    #  line[3:] = Message                               #
                    # ###################################################
                    message_list.append(make_message(line[2], line[0].split("!")[0].lstrip(":"), message.lstrip(":")))
        except socket.error:
            print("Error hit :(")
            pass
