#!/bin/env python3 
import requests 
import json

url = "http://web-09.challs.olicyber.it/login"
data = {"username": "admin", "password": "admin"}

header = {'Content-type': 'application/json'}

res = requests.post(url, data=json.dumps(data), headers=header)
print(res.text)

