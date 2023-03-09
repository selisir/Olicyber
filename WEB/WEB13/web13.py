#!/bin/env python3 
import requests
from bs4 import BeautifulSoup

url = "http://web-13.challs.olicyber.it/"
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

#seleziono solo le lettere rosse 
lettere = soup.find_all("span", {'class':"red"})

flag = ''
for span in lettere: 
    flag += span.text

print(flag)


