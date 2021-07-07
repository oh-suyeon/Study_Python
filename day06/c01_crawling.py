import requests
from bs4 import BeautifulSoup

url = 'http://localhost:8090/HELLOWEB2/hello.jsp'

response = requests.get(url) # 끌고 오는 역할

#print("status_code : ", response.status_code)
#print("text : ", response.text)

if response.status_code == 200 :
    html = response.text
    #soup = BeautifulSoup(html, 'html.parser')
    #title = soup.select_one('#rso > div:nth-child(3) > div > div > div.yuRUbf > a')
    #print(html)
    #print(title)
    #print(title.get_text())
else :
    print(response.status_code)