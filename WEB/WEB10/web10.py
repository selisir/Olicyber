#!/bin/env python3 
import requests 


url = "http://web-10.challs.olicyber.it/"
data = {"username": "admin", "password": "admin"}

header = {'Content-type': 'application/json'}

#opzionale: non serve ai fini della flag 
res = requests.options(url)
print(res.headers)  

res = requests.put(url)
print(res.headers)

