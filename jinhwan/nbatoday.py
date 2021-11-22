# nba 오늘의 경기 가져오기
import requests
from bs4 import BeautifulSoup
import re

url = "https://sports.news.naver.com/basketball/index"

html = requests.get(url)
bs_html = BeautifulSoup(html.content,"html.parser")

naver_logo = bs_html.find("div",{"id":"_tab_box_nba"})

nba = naver_logo.text 
nba_a = re.sub(r'[(기록|영상|응원)|\n|\t]', "", nba)
nba_a = re.sub(r'(종료)', '\n', nba_a)
# nba_a = re.sub(r'\d+', r'\g<0>\t',nba_a)\
nba_a = re.sub('(\\d+)(\\D+)(\\d+)(\\D+)','\\1\t\\2\t\\3\t\\4',nba_a)
new_msg = "nba 정보입니다.\n"
for line in nba_a.split('\n'):
    score_team = line.split('\t')
    for i, a in enumerate(score_team):
        if i % 2 == 0:
            new_msg += a.ljust(5, " ")
        else :
            count_num = len(a)
            new_msg += a + " "*(7-count_num)*2
    new_msg += '\n'
print(new_msg)




# print(nba_a)
# result = list(nba)
# while '\n' in result:
#     result.remove('\n')
# while '\t' in result:
#     result.remove('\t')    
# while '종' in result:
#     result.remove('종')
# while '료' in result:
#     result.remove('료')
# while '기' in result:
#     result.remove('기')
# while '록' in result:
#     result.remove('록')
# while '영' in result:
#     result.remove('영')
# while '상' in result:
#     result.remove('상')
# while '응' in result:
#     result.remove('응')
# while '원' in result:
#     result.remove('원')
# print(result)
# result_=''.join(result)

# print(result_)


