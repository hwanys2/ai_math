from konlpy.tag import Okt
import re  
okt = Okt()  

# 정규 표현식을 통해 온점을 제거하는 정제 작업.  
token = re.sub("(\.)","","정부가 발표하는 물가상승률과 소비자가 느끼는 물가상승률은 다르다.")  

# OKT 형태소 분석기를 통해 토큰화 작업을 수행한 뒤에, token에다가 넣음.  
token = okt.morphs(token)  

word2index = {}  
bow = []  
for voca in token:  
# token을 읽으면서, word2index에 없는 (not in) 단어는 새로 추가하고, 이미 있는 단어는 넘깁니다.   
         if voca not in word2index.keys():  
             word2index[voca] = len(word2index)  
             # BoW 전체에 전부 기본값 1을 넣는다.
             bow.insert(len(word2index)-1,1)
         else:
            # 재등장하는 단어의 인덱스
            index = word2index.get(voca)

            # 재등장한 단어는 해당하는 인덱스의 위치에 1을 더한다.
            bow[index] = bow[index]+1

print(word2index)  