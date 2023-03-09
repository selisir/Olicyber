#!/bin/env python3 
import requests 

url = "http://web-03.challs.olicyber.it/flag"
headers = {'X-password':'admin'}
res = requests.get(url, headers=headers)

print(res.text)

