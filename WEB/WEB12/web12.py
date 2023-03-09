import requests
from bs4 import BeautifulSoup

url = "http://web-12.challs.olicyber.it/"
res = requests.get(url)

soup = BeautifulSoup(res.content, 'html.parser')
#scelgo p perchè è il tag dei paragrafi 
paragrafi = soup.find_all('p')
print(paragrafi)

