import requests
from bs4 import BeautifulSoup

url = 'http://www.gwangju-highschool.hs.kr/main.php?menugrp=050101&master=meal2&act=list'

response = requests.get(url)
food_menu = []
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    food = soup.select_one('#meal_container > div.meal_content.col-md-7 > div > table > tbody > tr > td')
    food = food.get_text()
    print(food)
    # print(food.type())
else : 
    print(response.status_code)
    
food = food.replace('                        ','')

print(food)

# print(list(food))
# for i in range(10):
#     food.split('n')
# print(food_menu)

# for i in range(5):
#     food.sprit(' ')[i].append(food_menu)