fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]
fish_data = [[l,w] for l, w in zip(fish_length, fish_weight)]  # 이거 상당히 유용할듯.
fish_target = [1]*35+[0]*14  # 이건 data와 비슷하게 하되 111111111111100000 이런 느낌으로 만든다.

# 앞 35개는 도미, 뒤 14개는 빙어 임.
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()
print(fish_data[4])
print(fish_data[:3])
print(fish_data[47:])

train_input = fish_data[:35]
train_target = fish_target[:35] # 타겟의 의미는 도미인지 빙어인지 알려주는 것!!!
test_input = fish_data[35:]
test_target = fish_target[35:]

kn = kn.fit(train_input, train_target)  #훈련한다!
print(kn.score(test_input, test_target))  # 0.5는 절반 맞추었다. 1은 모두 맞추엇다!
# 0인이유는 도미만 공부시키고 빙어를 테스트했으니 문제가 생기는 것임. 해결하기위해 랜덤으로 섞어보자.

#--------------넘파이로 샘플을 조정하는 것
import numpy as np
input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

np.random.seed(42)  # 42번이라는 랜덤요소로 섞겠다는 것 이번호로 하면 항상 같은 결과의 랜덤값이 나옴
index = np.arange(49)
np.random.shuffle(index)
print(index)

train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]
test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]
print(train_target)
print(test_input)

#-----잘 섞였는지 봐보는것 ---------
# import matplotlib.pyplot as plt
# plt.scatter(train_input[:,0], train_input[:,1])
# plt.scatter(test_input[:,0], test_input[:,1])
# plt.show()

kn.fit(train_input, train_target)
print(kn.score(test_input, test_target))

print(kn.predict(test_input))


#------zip 함수 연습---------------------
# name = ['안종빈','박지성','손흥민','차범근']
# kick = [90,95,97,100]
# defence = [9,10,5,7]

# player_data = [[n,k,d] for n,k,d in zip(name,kick,defence)]
# print(player_data)