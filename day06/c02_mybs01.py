import requests
from bs4 import BeautifulSoup

url = 'http://localhost:8090/HELLOWEB2/hello.jsp'

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, 'html.parser')

all_td = soup.find_all('td')

for td in all_td :
    text = td.get_text()
    print(text)

print("-----------------------------")
    
tds = soup.select('td')

for idx, td in enumerate(tds) :
    if idx > 2 :
        print(td.text)
    
    
print("-----------------------------")

s_tds = soup.select('tr:nth-child(2) td')
for td in s_tds :
    text = td.text
    print("시진핑 : ", text)

l_tds = soup.select('tr:nth-child(3) td')
for td in l_tds :
    text = td.get_text()
    print("리커칭 : ", text)