#!/bin/env python3 
import requests
from bs4 import BeautifulSoup, Comment

url = "http://web-14.challs.olicyber.it/"
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

commenti = soup.find_all(string=lambda text: isinstance(text, Comment))

for c in commenti: 
    print(c)
    print("------")
    c.extract()


#flag{50m3b0dy_f0rg07_70_d31373_7hi5} 