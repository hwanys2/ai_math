import pandas as pd
import urllib.request
import os
# 15년 동안 발행된 뉴스 기사
#urllib.request.urlretrieve("https://raw.githubusercontent.com/franciscadias/data/master/abcnews-date-text.csv", filename="abcnews-data-text.csv")
path = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(path+'\\abcnews-data-text.csv', error_bad_lines=False)

text = data[['headline_text']]
text.head(5)

# 2. 텍스트 전처리
import nltk
text['headline_text'] = text.apply(lambda row: nltk.word_tokenize(row['headline_text']), axis=1)
 # NLTK의 word_tokenize통해 토큰화

#불용어 제거
from nltk.corpus import stopwords
stop = stopwords.words('english')
text['headline_text'] = text['headline_text'].apply(lambda x:[word for word in x if word not in(stop)])
# against,be, of, a , in , to등 단어 제거

# 표제어 추출 - 3인칭 단수 표현을 1인칭으로 변경, 과거 진행형 동사를 현재형
from nltk.stem import WordNetLemmatizer
text['headline_text'] = text['headline_text'].apply(lambda x:[WordNetLemmatizer().lemmatize(word,pos='v') for word in x])
text.head(5)

#3이하 단어 제거
tokenized_doc = text['headline_text'].apply(lambda x:[word for word in x if len(word) >3])

# 3. TF-IDF 행렬 만들기
detokenized_doc = []
for i in range(len(text)):
    t = ' '.join(tokenized_doc[i])
    detokenized_doc.append(t)
#역토큰화
text['headline_text'] = detokenized_doc # 다시 text['headline_text']에 재저장
#사이킷런 TF-IDF 행렬
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)#상위 1000개 단어 봅존
X = vectorizer.fit_transform(text['headline_text'])

# 4. 토픽 모델링
from sklearn.decomposition import LatentDirichletAllocation
lda_model = LatentDirichletAllocation(n_components=10,learning_method='online',random_state=777, max_iter=1)
lda_top=lda_model.fit_transform(X)

terms=vectorizer.get_feature_names() #단어 집합, 1000개의 단어가 저장됨

def get_topics(components, feature_names, n=5):
    for idx, topic in enumerate(components):
        print("Topic %d :" % (idx+1), [(feature_names[i], topic[i],round(2)) for i in topic.argsort()[:-n - 1:-1]])
get_topics(lda_model.components_, terms)