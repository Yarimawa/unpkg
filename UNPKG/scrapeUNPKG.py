"""
Python 3.7.5 -
    Python Web Scraper/Crawler Module.

    Scrapes 'unpkg.com' for npm pakages.
"""

import requests
from bs4 import BeautifulSoup
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# BASE_URL = "http://127.0.0.1:1234/"
timeout_delay = 60

BASE_URL = "https://www.unpkg.com/browse/"

def __process_folder(par_dir, cur_folder, par_url=''):
    """Returns the folders and files in the folder."""
    # create a new folder
    print('par_url >>', par_url)
    print(par_dir,'||', cur_folder)
    os.mkdir(os.path.join(par_dir, cur_folder))

    folders = []
    files = []

    r = requests.get(BASE_URL+par_url+cur_folder+'/', timeout=timeout_delay)
    print('r --', BASE_URL+par_url+cur_folder)
    print(r.status_code)
    
    soup = BeautifulSoup(r.text, 'lxml')

    data = soup.find('tbody').find_all('tr')

    for item in data:
        row_data = item.find_all('td')
        if row_data[2].text != '-':   # item is a file
            # check if item is a '..' - 'Parent directory link'
            if row_data[1].text == '..': # if true do not add as a file
                continue
            filedata = {'name': row_data[1].text, 'size': row_data[2].text, 'type': row_data[3].text}
            files.append(filedata)
            __process_file(os.path.join(par_dir, cur_folder), filedata, par_url+f'{cur_folder}/')
        elif row_data[2].text == '-':   # item is a folder
            folders.append(row_data[1].text)
            __process_folder(os.path.join(par_dir, cur_folder), row_data[1].text, par_url=par_url+cur_folder+'/')

    return 'Files - {}, Folders - {}'.format(len(files), len(folders))

# print(__process_folder('file', ''))

def __process_file(par_dir, file_, par_url):
    """Clones code snippet to local drive."""

    print("File - Passed")
    print(BASE_URL+par_url+file_['name'])
    r = requests.get(BASE_URL+par_url+file_['name'], timeout=timeout_delay)
    print(r.status_code)

    soup = BeautifulSoup(r.text, 'lxml')
    url = soup.find('div', class_='css-10o5omr').a['href']

    ext = ''
    if os.path.splitext(file_['name'])[1] == '' and file_['type'] == 'text/plain':
        ext = '.txt'

    with open(os.path.join(par_dir, file_['name']+ext), 'w') as f:
        try:
            r = requests.get(BASE_URL.replace('/browse/', '')+url, timeout=timeout_delay)
            print("Writing...")
            print(r.status_code)
            soup_ = BeautifulSoup(r.text, 'lxml')

            f.write(soup_.text)
            f.close()
            print("Done\n")
        except Exception:
            raise Exception
            # r = requests.get(BASE_URL+'raw')

if len(sys.argv) == 2:
    __process_folder(BASE_DIR, sys.argv[1])
    
    # r = requests.get(BASE_URL+'react-native/', timeout=timeout_delay)
    # print(r.status_code)
    
    # soup = BeautifulSoup(r.text, 'lxml')

    # print(__process_folder(BASE_DIR, 'react-native'))
    # print(__process_file(BASE_DIR, {'name':'file', 'size': '2.17kB', 'type': 'text/plain'}, ''))

else:
    raise ValueError(
                    "Invalid number of arguments passed.\n"+
                    "Run - python scrapeUNPKG.py *arg\n"+
                    ":param\n"+
                    "*arg: should be a package name\n"+
                    "\te.g. react-native"
                    )
