# # 오늘의 급식 가져오기
import requests
from bs4 import BeautifulSoup
url = 'http://gwangju.gen.hs.kr/main/main.php#none;'

response = requests.get(url)
food_menu = []
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    food = soup.select_one('#container > div.midbox > div.col_box.food > dl')
    food = food.get_text()
    food = food.replace("아침", "")
    food = food.replace("등록된 식단이 없습니다.","")
else : 
    print(response.status_code)
    
print(food)


import telegram

telgm_token = '2051505908:AAEnH-QNTu02HCNMHIO2mTbY4T09NWJq7Zo'

bot = telegram.Bot(token = telgm_token)



bot.sendMessage(chat_id = '2039207169', text= food)
