import sys, os
import requests
import base64
import getpass
import bs4
import json
import typing

ab_path = os.path.abspath(__file__)
cur_dir = os.getcwd()

master_pass = getpass.getpass()

content_from_urls = {'youtube' : 'https://www.youtube.com/user/ourbigdumbmouth',
                     'libsyn' : 'http://ourbigdumbmouth.libsyn.com/rss'}

content_to_urls = {'minds' : '',
                   'dtube' : '',
                   'bitchute' : '',
                   'steemit' : ''
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
    run_script()