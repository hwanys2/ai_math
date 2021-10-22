# nba 오늘의 경기 가져오기
import requests
from bs4 import BeautifulSoup

url = 'https://sports.news.naver.com/basketball/schedule/index?category=nba'

response = requests.get(url)
food_menu = []
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    food = soup.select_one('#content > div.sch_volleyball.tb_nba')
    food = food.get_text()
    food = food.replace('\n','')
    print(food)
    food_menu.append(food)
    # print(food.type())
else : 
    print(response.status_code)