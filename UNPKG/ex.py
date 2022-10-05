import requests
from bs4 import BeautifulSoup

class Leaf:
    """A Leaf represents a folder containing sub-directories and/or files."""
    def __init__(self, name):
        self.name = name
        self.files = []  # E.g. {'name': 'RCTAssert.h', 'size': '6.68 kB', 'type': 'text/x-c'}
        self.folders = []

    def __send_request(self, url):
        r = requests.get(url)
        self.__scrape(r)

    def __scrape(self, r):
        soup = Beautiful(r.text, 'lmxl')
        rows = soup.find('tbody').find_all('tr')
        self.__handle_rows(rows)

    def __handle_rows(self, rows):
        for row in rows:
            row_datum = item.find_all('td')
            if row_datum[2].text != '-':   # data is a file
                # check if data is a '..' - 'Parent directory link'
                if row_datum[1].text == '..': # if true do not add as a file
                    continue
                self.files.append({'name': row_datum[1].text, 'size': row_datum[2].text, 'type': row_datum[3].text})
            elif row_datum[2].text == '-':   # data is a folder
                self.folders.append(row_datum[1].text)
    
    def build(self):
        self.__send_request()
    
    def get_files(self):
        return self.files
        
    def get_folders(self):
        return self.folders
        
    def __str__(self):
        return self.name
