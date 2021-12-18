fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

import numpy as np
fish_data = np.column_stack((fish_length, fish_weight))
print(type(fish_data))   # 튜플로 연결해버린것임.
fish_target = np.concatenate((np.ones(35), np.zeros(14)))

from sklearn.model_selection import train_test_split

#train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, random_state = 42)
train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, stratify = fish_target, random_state = 42) 
#stratify=fish_target 넣으면 전체 비율과 비슷하게 맞추어줌.
# print(train_input.shape, test_input.shape)
# print(train_target.shape, test_target.shape)

#print(test_target)
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()
kn.fit(train_input, train_target)
# print(kn.score(test_input,test_target))
# print(kn.predict([[25, 150]]))  # 엥?  내가 공부시킨거로 보면 이놈은 1이 나와야 하는데 0(빙어)가 나오네?
# 내가 예측한 (25,150) 이놈을 그래프로 위치 찾아본 것
import matplotlib.pyplot as plt
# plt.scatter(train_input[:,0],train_input[:,1])
# plt.scatter(25,150,marker='^')
# plt.show()   #아무리 봐도 도미에 가까운데....?
# 이유는 가까운 이웃의 샘플중 다수인 클래스를 예측으로 사용함(기본값 5개)
# 한번 거리를 구해가보자
# distances, indexes = kn.kneighbors([[25,150]]) # 주변 5개를 D로 칠해라!!!

# plt.scatter(train_input[:,0], train_input[:,1])
# plt.scatter(25,150,marker ='^')
# plt.scatter(train_input[indexes,0], train_input[indexes,1], marker='D')
# plt.show()   # 그래프를 x축 y축 같게하면 됨. 그래서 0이라고 추측한 것임!!

# 그래서 데이터전처리과정이 필요하다!!!! 표준점수형태로 하자. 즉 데이터-평균/표준편차
mean = np.mean(train_input, axis=0)
std = np.std(train_input, axis=0)

train_scaled = (train_input-mean) / std
test_scaled = (test_input-mean) / std
print(train_scaled)

new = ([25,150]-mean) / std
kn.fit(train_scaled, train_target)
distances, indexes = kn.kneighbors([new])
plt.scatter(train_scaled[:,0],train_scaled[:,1])
plt.scatter(new[0], new[1], marker='^')
plt.scatter(train_scaled[indexes,0], train_scaled[indexes,1], marker='D')
plt.show()


print(kn.score(test_scaled,test_target))

kn.predict([new])