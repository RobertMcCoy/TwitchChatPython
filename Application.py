import urllib.request
import json
from Channel import Channel
from ApiHelper import ApiHelper

LIMIT_PER_THREAD = 40
STREAMER_API_URL = 'https://api.twitch.tv/kraken/streams?access_token=' \
                   '&client_id=i3fyf84w4iies7v78jov1jp2zmwdbpa&limit=1'


def get_streamers_count():
    json_data = json.loads(urllib.request.urlopen(urllib.request.Request(STREAMER_API_URL)).read())
    return int(json_data['_total'] / 100.0) * 100

max_streamers = get_streamers_count()
thread_list = []


for count in range(0, max_streamers, LIMIT_PER_THREAD):
    thread_list.append(ApiHelper(count).start())
