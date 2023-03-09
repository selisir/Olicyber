#!/bin/env python3 
import requests 

url = "http://web-07.challs.olicyber.it/"

res = requests.head(url)
print(res.headers)

#flag{r0gu3_m374d474}