#!/bin/env python3 
import requests

url = "http://web-11.challs.olicyber.it/login"
data = {'username': 'admin', 'password': 'admin'}
session = requests.Session()
response = session.post(url, json=data)
csrf_token = response.json()['csrf']

flag_piece = []

for i in range(4):
   #qui non uso la variabile url ma preferisco mettere direttamente l'url
    response = session.get(f'http://web-11.challs.olicyber.it/flag_piece?index={i}&csrf={csrf_token}')
    csrf_token = response.json()['csrf']
    flag_piece.append(response.json()['flag_piece'])

flag_piece = ''.join(flag_piece)
print(flag_piece)

