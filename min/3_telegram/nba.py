# nba 오늘의 경기 가져오기
import requests
from bs4 import BeautifulSoup
import unicodedata

## 0. python용 줄맞춤
def fill_space(input_s="", max_size=40, fill_char=" "):
    # 길이가 긴 문자는 2칸으로 체크하고, 짧으면 1칸으로 체크함 / 남은 문자를 fill_char로 채운다.
    l = 0
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l+=2
        else:
            l+=1
    return input_s + fill_char*(max_size-l)

## 0. telegram 줄맞춤
strFormat = '%-14s%-4s%-3s%-4s%s\n'

msgTel = ""


## 1. beautifulsoup
url = "https://sports.news.naver.com/basketball/index"
html = requests.get(url)
bs_html = BeautifulSoup(html.content,"html.parser")


## 2. data 추출 및 정제
msg =""
#구조 .hmb_list_items > .vs_list > .score / .name 있음
nba_list = bs_html.select("#_tab_box_nba .hmb_list_items")
# 2팀씩 그룹핑 된 친구들
for nbaTeams in nba_list:
    teams = []
    scores = []
    time = nbaTeams.select(".state .time")  # 방송예정과 경기결과 구분을 위한 조건

    #2팀씩 세부
    for nbaTeam in nbaTeams.select(".vs_list"):
        teamNm = nbaTeam.select(".name")[0].get_text()
        if(len(nbaTeam.select(".win")) != 0):
            teamNm += "(승)"

        teams.append(teamNm)
        if(len(time) == 0): # 시간이 없어야 점수가 존재
            scores.append(nbaTeam.select(".score")[0].get_text().replace('\n',"").replace('\t',""))

    # 시간이 있으면 방송 예정 / 없으면 경기결과 출력
    if(len(time) != 0):
        time = time[0].get_text()
        msg += fill_space(teams[0], max_size=15)    #첫번째 팀
        msg += fill_space("vs", max_size=3)         # vs
        msg += fill_space(teams[1],max_size=15)     #첫번째 점수
        msg += time + "\n"
    else:
        # 0. python용 줄맞춤
        msg += fill_space(teams[0], max_size=15)    #첫번째 팀
        msg += fill_space(scores[0],max_size=4)     #첫번째 점수
        msg += fill_space("vs", max_size=3)         # vs
        msg += fill_space(scores[1],max_size=5)     #두번째 점수
        msg += teams[1]+"\n"                        #두번째 팀

        # 0. 텔레그램용 줄맞춤
        msgTel += strFormat % (teams[0],scores[0],'vs', scores[1], teams[1])


print(msg)
#print(msgTel)


## 3. telegram
#import telegram
#telgm_token = '2051505908:AAEnH-QNTu02HCNMHIO2mTbY4T09NWJq7Zo'
#bot = telegram.Bot(token = telgm_token)
#bot.sendMessage(chat_id = '2039207169', text= msg)