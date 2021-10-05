from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument("--use-fake-ui-for-media-stream")

url = 'https://www.google.com/webhp?hl=ko&sa=X&ved=0ahUKEwjVycHk9_vyAhXHyIsBHU0LBHkQPAgI'

# 음성인식 후 그 단어를 다시 가져오는 방법 연구하자
chromedriver = r'd:\\python\\chromedriver.exe'
driver = webdriver.Chrome(chromedriver, options=options)
driver.get(url)

loca = driver.find_element_by_class_name('XDyW0e')
loca.click()

time.sleep(5)

search = driver.find_element_by_xpath('//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')
voice = search.get_attribute("value")

# driver.quit()

url = 'https://www.youtube.com/results?search_query={0}'.format(voice + "듣는노래")
# chromedriver = r'd:\\python\\chromedriver.exe'
# driver = webdriver.Chrome(chromedriver)
driver.get(url)

loca = driver.find_element_by_class_name('style-scope yt-img-shadow')
loca.click()

# a = news.get_attribute("Content")
# print(a)
