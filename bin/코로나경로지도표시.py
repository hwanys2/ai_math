import folium as g
from selenium import webdriver
import time
import pyautogui
import pyperclip

chromedriver = r'd:\\python\\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.gwangju.go.kr/c19/contentsView.do?pageId=corona30')

tr_list = driver.find_elements_by_xpath('//*[@id="co_table"]/tr')

locate = []
date = []
for tr in tr_list:
    td_list = tr.find_elements_by_tag_name("td")
    locate.append(td_list[5].get_attribute("textContent"))
    date.append(td_list[0].get_attribute("textContent"))
locate = list(locate)
driver.quit()

g_map = g.Map(location=[35.1024693,126.8790725],zoom_start=13)

for i in range(1):
    chromedriver = r'd:\\python\\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver)
    driver.get('https://www.google.com/maps/@35.1683756,126.9218576,15z?hl=ko')

    a = str(locate[i])
    time.sleep(3)
    print(a)
    pyperclip.copy(a)     # pyperclip 를 가져온 건 한글이 안쳐지기 때문
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')


    time.sleep(3)
    c_url = driver.current_url
    print(c_url)
    k = int(c_url.find("@"))
    post = c_url[k+1:k+23]
    print(post)    # 35.135,128.010  이렇게 뜨는데 2개의 숫자가 아닌 '3''5''.''1''3''5' 이렇게 각각의 문자로 인식하는 문제가 생김

    b = post.split(',')
    c = b[0]
    d = b[1]
    marker = g.Marker([c,d], popup = date[i] , icon = g.Icon(color='red'))
    marker.add_to(g_map)
    driver.quit()
g_map.save('filename.html')

# chromedriver = r'd:\\python\\chromedriver.exe'
# driver = webdriver.Chrome(chromedriver)
# driver.get('https://www.google.co.kr/maps/@35.1683704,126.9218479,15z')

# time.sleep(1)
# pyautogui.typewrite(locate[0])
# pyautogui.press('enter')

# g_map = g.Map(location=[35.1660033,126.9329369],zoom_start=18)
	
# # g_map.save('filename.html')
# for tr in tr_list:
#     td_list = tr.find_elements_by_tag_name("td")
#     # date = td_list[0].get_attribute("textContent")
#     locate = td_list[4].get_attribute("textContent")
#     print(locate)

# locate = list(locate)
# driver.quit()
