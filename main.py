import time
import os
from qbittorrent import Client
from requests.exceptions import HTTPError


QB_URL = os.getenv('QB_URL')
QB_VERIFY = os.getenv('QB_VERIFY', False) == 'true'
QB_USER = os.getenv('QB_USER')
QB_PASS = os.getenv('QB_PASS')
SLEEP = 60


qb = Client(QB_URL, verify=QB_VERIFY)
qb.login(QB_USER, QB_PASS)

while True:
    torrents = qb.torrents()
    
    for torrent in torrents:
        # if '727' in torrent['name']:
        #     pass

        if torrent['trackers_count'] != 1:
            continue

        if torrent['category'] != '':
            continue

        if len(torrent['tracker']) == 0:
            continue

        site = torrent['tracker'].split('/')[2].split(':')[0].split('.')[-2]
        try:
            qb.set_category([torrent['infohash_v1'], ], site)
            print(torrent['name'], '->', site)
        except HTTPError as e:
            if e.response.status_code == 409:
                qb.create_category(site)
                qb.set_category([torrent['infohash_v1'], ], site)
    
    time.sleep(SLEEP)
