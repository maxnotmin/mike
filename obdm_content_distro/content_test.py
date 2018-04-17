import sys, os
import requests
import base64
import getpass
import bs4
import json
import typing
import feedparser
import re
import time
from datetime import datetime
import requests


ab_path = os.path.abspath(__file__)
cur_dir = os.getcwd()

def load_config():
    pass

#master_pass = getpass.getpass()

content_from_urls = {'youtube' : 'https://www.youtube.com/user/ourbigdumbmouth',
                     'libsyn' : 'http://ourbigdumbmouth.libsyn.com/rss'}



def get_podcast_data():
    try:
        rawPod = feedparser.parse(content_from_urls['libsyn'])
        podEntries = rawPod.entries
        recent_pod = []
        for j in podEntries[0]:
            recent_pod.append({
                'podTitle': j.title,
                'podURL': j.links[1].href,
                'podDate': str(j.published).replace('+0000', ''),
                'podSummary': re.sub("<.*?>", "", j.summary),
                'podImage': j.image['href']
            })
        #print(podList)
        return recent_pod
    except Exception as e:
        print("GET PODCAST ERROR: ", e)

def get_youtube_date():
    req = requests.get('https://www.youtube.com/user/ourbigdumbmouth')
    print("TEST REQ: ", req.text)






content_to_urls = {'minds': '',
                   'dtube': '',
                   'bitchute': '',
                   'steemit': ''
                   }

########   DATABASE INTERACTIONS
def connect_to_db():
    pass

def update_db():
    pass

def sweep_db():
    pass

def get_data_from_db():
    pass

def clean_content():
    pass

def get_content():
    # DOWNLOAD VIDEO FROM YOUTUBE

    # GET TITLE OF VIDEO

    # GET DESCRIPTION OF VIDEO

    # CONVERT DATA TO JSON ----- clean_content()

    # RETURN JSON
    pass




def throw_content():
    # SEND JSON TO URLS
    pass

def run_script():
    pass


if __name__ == "__main__":
    get_youtube_date()