#!/bin/env python3 
import requests 

url = "http://web-04.challs.olicyber.it/users"
headers = {'Accept': 'application/xml'}

print("Primo modo: ")
res = requests.get(url)
print(res.text)

print("Secondo modo: ")
res = requests.get(url, headers=headers)
print(res.text)

