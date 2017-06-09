import urllib.request
import json
import threading
from Channel import Channel

LIMIT_PER_THREAD = 40
STREAMER_API_URL = 'https://api.twitch.tv/kraken/streams?access_token=&' \
                   + 'client_id=i3fyf84w4iies7v78jov1jp2zmwdbpa&limit=' + str(LIMIT_PER_THREAD) + '&offset='


class ApiHelper(threading.Thread):
    def __init__(self, offset):
        threading.Thread.__init__(self)
        self.offset = offset

    def run(self):
        streamer_list = create_channel_list(self.offset)
        if 'twitchmedia_qs_10' in streamer_list:
            streamer_list.remove("twitchmedia_qs_10")
        return Channel(int(self.offset / LIMIT_PER_THREAD),
                       "Thread %s" % int(self.offset / LIMIT_PER_THREAD),
                       streamer_list).start()


def create_channel_list(offset):
    json_data = json.loads(urllib.request.urlopen(urllib.request.Request(STREAMER_API_URL + str(offset))).read())
    streamers = []
    for items in json_data['streams']:
        streamers.append(items['channel']['name'])
    return streamers
