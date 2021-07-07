import os
import sys
import urllib.request
from bs4 import BeautifulSoup

client_id = "CFEORhlvpTBvMzj1e5JZ"
client_secret = "7eBvAte0zd"

encText = urllib.parse.quote("주식")

url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText #  xml 결과

request = urllib.request.Request(url)

request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    html = response_body.decode('utf-8') 
    soup = BeautifulSoup(html, 'html.parser') #xml로 가져오면 item.pubDate.text로 가져와도 None이 아니라 제대로 값이 나온다.  

    xmlItems = soup.select('item')

    for item in xmlItems :
    
        title = item.select_one('title').text
        description = item.select_one('description').text
        pubDate = item.select_one('pubDate').text
        
        print("제목 : ", title)
        print("설명 : ", description)
        print("발행일 : ", pubDate)
        print("--------------------------------------------------------------------------------")

    
else:
    print("Error Code:" + rescode)