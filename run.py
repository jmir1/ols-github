import requests as reqs
from bs4 import BeautifulSoup
import json
import uuid
from socketIO_client import SocketIO
import time
import olsync.olclient
import os

USERNAME = '' #CHANGE THIS
PASSWORD = '' #CHANGE THIS

olc = olsync.olclient.OverleafClient()
olc.login(USERNAME, PASSWORD)
projects = olc.all_projects()
projectnames = [item['name'] for item in projects]
for item in projectnames:
  if not os.path.isdir(item):
    os.system('mkdir "' + item + '"')
    os.system('cp .olauth "' + item + '/.olauth"')
    os.system('cd "' + item + '" && git pull')
    os.system('cd "' + item + '" && ols')
    os.system('git add . && git commit . -m "update ' + item + '"')
    print(item)
  else:
    os.system('cd "' + item + '" && git pull')
    os.system('cd "' + item + '" && ols')
    os.system('git add . && git commit . -m "update ' + item + '"')
os.system('git push')
