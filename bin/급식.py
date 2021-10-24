import requests
from bs4 import BeautifulSoup
url = 'http://gwangju.gen.hs.kr/main/main.php#none;'

response = requests.get(url)
food_menu = []
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    food = soup.select_one('#container > div.midbox > div.col_box.food > dl > dd.r_second')
    food = food.get_text()
    food = food.replace("아침", "")
    food = food.replace("등록된 식단이 없습니다.","")
else : 
    print(response.status_code)
    
print(food)