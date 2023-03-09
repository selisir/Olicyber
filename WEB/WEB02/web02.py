#!/bin/env python3 
import requests 

url = "http://web-02.challs.olicyber.it/server-records"
payload = {'id':'flag'}

res = requests.get(url, params=payload)

print(res.text)

