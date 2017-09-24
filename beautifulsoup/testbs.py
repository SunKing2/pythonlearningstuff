'''
Created on Jun 1, 2017

@author: louie
'''

import requests
from bs4 import BeautifulSoup

htmlpage = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
page = htmlpage.text
print(page)
soup = BeautifulSoup(page)
myspans = soup.find_all('span')
print (type(myspans))
for sps in myspans:
    print(sps.string)

if __name__ == '__main__':
    pass