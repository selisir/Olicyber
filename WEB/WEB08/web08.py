#!/bin/env python3 
import requests 

url = "http://web-08.challs.olicyber.it/login"
dati = {"username": "admin", "password": "admin"}

res = requests.post(url, data=dati)
print(res.text)

