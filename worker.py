import requests

from termcolor import colored


import threading
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


TEST_URL = 'https://kith.com/collections/all'


class Worker(threading.Thread):
    def __init__(self, id, proxy):
        threading.Thread.__init__(self)
        self.id = id
        self.proxy = proxy

        parts = self.proxy.split(':')
        self.s = requests.Session()
        self.s.verify = False
        self.s.proxies.update({
            'http': 'http://{}:{}@{}:{}'.format(parts[2], parts[3], parts[0], parts[1]),
            'https': 'https://{}:{}@{}:{}'.format(parts[2], parts[3], parts[0], parts[1])
        })
        self.s.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Content-Type': '',
            'Accept': '*/*'
        })

    def run(self):
        r = self.s.get(
            TEST_URL
        )
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            print colored(
                '[#{}] [bad] [T:{}] {}'.format(
                    str(self.id).zfill(3),
                    str(r.elapsed.total_seconds()).ljust(10, '0'),
                    self.proxy
                ),
                'red'
            )
        if r.status_code == 200:
            print colored(
                '[#{}] [good] [T:{}] {}'.format(
                    str(self.id).zfill(3),
                    str(r.elapsed.total_seconds()).ljust(10, '0'),
                    self.proxy
                ),
                'green'
            )
