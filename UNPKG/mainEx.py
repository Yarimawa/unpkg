import requests
from bs4 import BeautifulSoup
import sys
from PackageError import *
import socket
import uuid
import imghdr
import os

# print(os.path.dirname(os.path.abspath(__file__)))

# hostname = socket.gethostname()
# IP = socket.gethostbyname(hostname)
# print(IP)

r = requests.get("http://127.0.0.1:1234/raw")
soup = BeautifulSoup(r.text, 'lxml')
print(soup.find('pre').text)