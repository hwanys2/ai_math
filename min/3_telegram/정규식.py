# nba 오늘의 경기 가져오기
import requests
from bs4 import BeautifulSoup
import re

url = "https://sports.news.naver.com/basketball/index"

html = requests.get(url)
bs_html = BeautifulSoup(html.content,"html.parser")

naver_logo = bs_html.find("div",{"id":"_tab_box_nba"})

nba = naver_logo.text


import re
nba = naver_logo.text
nba_a = re.sub(r'[(기록|영상|응원)|\n|\t]','', nba)
nba_a = re.sub(r'(종료)','\n', nba_a)
nba_a = re.sub(r'\d+','\t\g<0> ', nba_a)
print(nba_a)

#정규식
# [] -> 패턴
# |  -> or
# () -> 문자
# re.sub()  -> 해당 패턴은 제외 후 문자열 출력
# \d -> 숫자패턴 [0-9]
# +  -> 앞 문자가 하나 이상임
# \g<0> -> 파이썬에서 전체 일치부를 치환 텍스트에 삽입하려면 \g<0>이라는 토큰을 사용