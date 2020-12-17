import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    number = music.select_one('td.number')
    numberstrip = number.text[0:2].strip() #text[0.2] 확인
    title = music.select_one('td.info > a.title.ellipsis')
    titlestrip = title.text.strip()
    singer = music.select_one('td.info > a.artist.ellipsis')
    singerstrip = singer.text.strip()
    #print(numberstrip, titlestrip, singerstrip)
    doc = {
        'numberstrip': numberstrip,
        'titlestrip': titlestrip,
        'singerstrip': singerstrip
    }
    db.musics.insert_one(doc)