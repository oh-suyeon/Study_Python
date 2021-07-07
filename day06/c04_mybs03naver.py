import requests
from bs4 import BeautifulSoup

f = open("stock.xml", "rt", encoding='UTF8')
xml = f.read()

soup = BeautifulSoup(xml, 'html.parser')

xmlItems = soup.select('item')

for item in xmlItems :
    
    title = item.select_one('title').text
    description = item.select_one('description').text
    pubDate = item.select_one('pubDate').text
    
    print("제목 : ", title)
    print("설명 : ", description)
    print("발행일 : ", pubDate)
    print("--------------------------------------------------------------------------------")

