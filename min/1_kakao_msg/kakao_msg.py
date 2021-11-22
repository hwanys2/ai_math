# 목적 : 아침마다 IT 뉴스 수집
# 조건
# - IT뉴스 Headlight 수집
# - 검색에 휴대폰은 제외
# - 시간 - 제목으로 출력
# - 아침 7시마다 작동

# - 해당 내용 파일로 저장
# - 해당 내용 카카오톡으로 받아보기
# - 중지는 키보드 ESC 입력 시
# driver.implicitly_wait(10) # seconds

# 셀레니움 선언
from selenium import webdriver
import time
import json

# chrome driver 옵션
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["enable-logging"])   # 크롬드라이버 실행될때 로그 해지
driver = webdriver.Chrome("chromedriver", options=options)


# 1. 브라우저 이동
driver.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105")

# 2. headline 수집
#var excludeVoca = {'폰','휴대폰','갤럭시','아이폰'}
items   = []
inItems = {}
title_as = driver.find_elements_by_css_selector('#section_body dt:not(.photo) a')   # id가 setion_body < 아래객체중에 dt태그 < 그 중 class명이 photo 제외 < a태그
for title_a in title_as:
    text = title_a.get_attribute('text')
    if '폰' in text or '휴대폰' in text or '갤럭시' in text or '아이폰' in text:    #불필요한 문자열(폰,휴대폰,아이폰) 배열에서 포함된 애들
        continue    #반복문 넘김 => 아래로직 안 돌고 다시 for문 맨처음으로 돌아감
    else:
        href = title_a.get_attribute('href')
        inItems.update({'title' : text,'link':{'web_url' : href,'mobile_web_url' : href }})

#jsonVal = json.dumps(inItems)
jsonVal = inItems
items.append(jsonVal)

# 5. 파일로 저장

# 6. 카카오톡으로 저장
#json token 호출
import datetime
import requests

import kakao_token as kToken

# 현재시간
headerTitle = datetime.datetime.now().strftime("%Y-%m-%d") + ' news'
#kToken.getNewToken()
with open(r"D:\Project\py\study\kakao_code.json","r") as fp:
  tokens = json.load(fp)


# 나 /v2/api/talk/memo/default/send
# 친구 /v1/api/talk/friends/message/default/send
send_url= "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers={"Authorization" : "Bearer " + tokens["access_token"]}
data={
     "template_object": json.dumps({
        "object_type":"text",
        "header_title":headerTitle,
        "header_link" : {
            "web_url" : "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105",
            "mobile_web_url" : "https://m.news.naver.com/main?mode=LSD&sid1=105"
        },
        "text" : "메시지 전송"
    })
}

# 친구
print(data)
response = requests.post(send_url, headers=headers, data=data)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))


print(response)
print(response.status_code)

if '401' == response.status_code:
    kToken.getNewToken()


#401 -> 403

#[contains(text(), 'Matty Matheson Hood')][not(contains(text(),'Tie Dye'))]

# #section_body>ul>li>dl>dt>a
#$("#section_body>ul>li dt").not(".photo")
#$("#section_body dt:not(.photo) a")
#$("#section_body dt:not(.photo) a:not(:contains('폰'))").filter(":not(:contains('에이즈'))").length

time.sleep(180)
driver.quit()




# 친구 전송
# friend_url = "https://kapi.kakao.com/v1/api/talk/friends"
# headers={"Authorization" : "Bearer " + tokens["access_token"]}
# result = json.loads(requests.get(friend_url, headers=headers).text)
# print(type(result))
# friends_list = result.get("elements")
# friend_id = friends_list[0].get("uuid")
# send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
# data={
#     'receiver_uuids': '["{}"]'.format(friend_id),
#     "template_object": json.dumps({
#         "object_type":"text",
#         "text":"성공입니다!",
#         "link":{
#             "web_url":"www.daum.net",
#             "web_url":"www.naver.com"
#         },
#         "button_title": "바로 확인"
#     })
# }
# response = requests.post(send_url, headers=headers, data=data)
# response.status_code


# 3. headline dt태그 형제 중 필요없는 이름 제외
#as = driver.find_elements_by_css_selector('#section_body dt:not(.photo) a')
#as = driver.find_elements_by_css_selector('#section_body dt:not([class=photo]) a')
#for a in as:,
 #   print(a.get_attribute('text') + '\t href=' +a.get_attribute('href'))

# 4. headline a태그 중 휴대폰,폰 항목이 안들어가는 친구들
#dts = driver.find_elements_by_css_selector('#section_body dt:not(.photo) a:not(:contains("폰"))')
#dts = driver.find_elements_by_xpath('//*[@id="section_body"][contains(text(),"폰")]')
#dts = driver.find_elements_by_css_selector('#section_body a[contains(text(),"폰")]')
#dts = driver.find_elements_by_css_selector('#section_body dt:not(.photo) a[textContent *="코로나"]')
#dts2 = driver.find_elements_by_css_selector('#section_body dt:not(.photo) a[innerHTML *="코로나"]')
#dts3 = driver.find_elements_by_css_selector('#section_body dt:not(.photo) a[text *="코로나"]')
#dts4 = driver.find_elements_by_css_selector('#section_body dt:not(.photo) a[title *="코로나"]')


#https://ai-creator.tistory.com/23