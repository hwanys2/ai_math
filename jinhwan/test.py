corona = {}
corona[1] = {'locate' : '전남대', 'date' : '2021-10-04'}
corona[2] = {'locate' : '광주고', 'date' : '2021-10-03'}


print(corona[1]['date'])

fruit = {'사과' : 'apple', '바나나': 'banana'}
print(fruit['사과'])
url = 'https://www.google.com/maps/place/%EA%B4%91%EC%A3%BC%EA%B4%91%EC%97%AD%EC%8B%9C+%EC%84%9C%EA%B5%AC+%EC%8C%8D%EC%B4%8C%EB%8F%99+%EC%83%81%EC%9D%BC%EB%A1%9C54%EB%B2%88%EA%B8%B8+9-3/@35.1603546,126.8620776,17z/data=!3m1!4b1!4m5!3m4!1s0x35718eab34597159:0x26e11e41f3b3960b!8m2!3d35.1603546!4d126.8642663?hl=ko'
print(float(url.split('@')[1].split(',')[0]))
print(float(url.split('@')[1].split(',')[1]))
# user_name = os.popen('git config --list ').read().split('user.name=')[1].split('\n')[0]