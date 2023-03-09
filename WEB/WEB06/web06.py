#!/bin/env python3 
import requests 

#qui prendo il cookie
url = " http://web-06.challs.olicyber.it/token"
token = requests.Session()

res = token.get(url)

#adesso posso accedere per la flag
url = "http://web-06.challs.olicyber.it/flag"
res = token.get(url)
print(res.text)

