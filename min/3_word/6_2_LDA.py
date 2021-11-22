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

# 1) 정수 인코딩과 단어 집합
# 단어 정수 인코딩, 단어의 빈도수 = (word_id, word_frequency)
from gensim import corpora
dictionary = corpora.Dictionary(tokenized_doc)
corpus = [dictionary.doc2bow(text) for text in tokenized_doc]


# 2) LDA모델 훈련
import gensim
NUM_TOPICS = 20 # 20개의 토픽, k=20
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
#topics = ldamodel.print_topics(num_words=4)
#for topic in topics:
#print(topic)

# 3) LDA 시각화 하기
#import pyLDAvis
#import pyLDAvis.gensim_models as gensimvis

#pyLDAvis.enable_notebook()
#pyLDAvis.display(vis)
#vis = gensimvis.prepare(ldamodel, corpus, dictionary)
#pyLDAvis.save_html(vis, 'LDA_Vis.html')

# 4) 문서별 토픽 분포 보기
#for i, topic_list in enumerate(ldamodel[corpus]):
 #   if i==5:
 #       break
  #  print(i, '번째 문서의 topic 비율은 ', topic_list)

def make_topictable_per_doc(ldamodel, corpus):
    topic_table = pd.DataFrame()

    #몇 번째 문선인지 의미하는 문서번호화 해당 문서의 토픽 비중을 한 줄 씩 꺼내온다.
    for i, topic_list in enumerate(ldamodel[corpus]):
        doc = topic_list[0] if ldamodel.per_word_topics else topic_list
        doc = sorted(doc, key=lambda x: (x[1]), reverse=True)
        # 각 문서에 대해 비중이 높은 토픽순으로 토픽을 정렬
        # ex) 정렬 전 0번 문서 : (2번 토픽, )

        #모든 문서에 대해 아래 수행
        for j, (topic_num, prop_topic) in enumerate(doc):
            if j == 0:  # 정렬을 한 상태이므로 가장 앞에 비중 높은 토픽
                topic_table = topic_table.append(pd.Series([int(topic_num), round(prop_topic,4), topic_list]), ignore_index=True)
                # 비중높은 토픽, 비중, 전체 토픽 비중
            else:
                break
    return(topic_table)

topictable = make_topictable_per_doc(ldamodel, corpus)
topictable = topictable.reset_index() # 문서번호 의미 열(column)을 사용하기 위해 인덱스 열하나 더 만듬
topictable.columns=['문서번호', '가장 비중 높은 토픽', '가장 높은 토픽의 비중', '각 토픽의 비중']
topictable[:10]
print(topictable)
