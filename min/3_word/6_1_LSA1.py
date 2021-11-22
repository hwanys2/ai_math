import pandas as pd
from sklearn.datasets import fetch_20newsgroups #scikit-learn에서 20 newsgroup 데이터를 받을수 있는 함수임
dataset = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers','footers','quotes'))
documents = dataset.data

dataset.target_names #카테고리 20개

#텍스트 전처리

news_df = pd.DataFrame({'document':documents})
# 특수문자 제거
news_df['clean_doc']=news_df['document'].str.replace("[^a-zA-Z]"," ")
# 길이가 3이하인 단어 제거(길이가 짧은 단어])
news_df['clean_doc']=news_df['clean_doc'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))
# 전체 단어 소문자
news_df['clean_doc']=news_df['clean_doc'].apply(lambda x: x.lower())

# 불용화
from nltk.corpus import stopwords

stop_words = stopwords.words('english') #NLTK로부터 불용어를 받아옵니다.
tokenized_doc = news_df['clean_doc'].apply(lambda x: x.split()) # 토큰화
tokenized_doc = tokenized_doc.apply(lambda x: [item for item in x if item not in stop_words]) # 불용어 제거

# 3) TF-IDF 행렬 만들기
# 역토큰화
detokenized_doc = []
for i in range(len(news_df)):
    t = ' '.join(tokenized_doc[i])
    detokenized_doc.append(t)

news_df['clean_doc'] = detokenized_doc

# TfidfVectorizer 통해 1000개의 단어의 TF-IDF 행렬
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000, max_df=0.5, smooth_idf=True)
X = vectorizer.fit_transform(news_df['clean_doc'])
#X.shape

# 4) 토픽 모델링
import numpy as np
from sklearn.decomposition import TruncatedSVD
svd_model = TruncatedSVD(n_components=20, algorithm='randomized', n_iter=100, random_state=122)
svd_model.fit(X)
len(svd_model.components_)  # svd_model.components_ VT임
#print(np.shape(svd_model.components_)) # 토픽의 수 t X 단어의 수 20X1000
terms = vectorizer.get_feature_names() # 단어 집합 1,000개의 단어가 저장됨

def get_topics(components, feature_names, n=5):
    for idx, topic in enumerate(components):
        print("Topic %d:" % (idx+1), [(feature_names[i], topic[i].round(5)) for i in topic.argsort()[:-n - 1:-1]])

get_topics(svd_model.components_, terms)

# 빠르게 구현 가능, 잠재적 의미 이끌어 낼 수 있어 좋은 성능을 냄, 새로운 데이터가 있을 경우 처음부터 다시 계산
