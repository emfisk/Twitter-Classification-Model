#!/usr/bin/python3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

df=pd.read_csv('githubdata.csv',nrows=5224)

useful_labels=pd.notnull(df.label)
labels=df.label
useful=pd.notnull(df['text'])
x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.2, random_state=7)
ns_probs = [0 for _ in range(len(y_test))]

tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7, encoding='utf-8')

tfidf_train=tfidf_vectorizer.fit_transform(x_train)
tfidf_test=tfidf_vectorizer.transform(x_test)


r_probs = model.predict_proba(tfidf_train)
ns_probs = [0 for _ in range(len(tfidf_test))]
scikit_log_reg = LogisticRegression(verbose=1, solver='liblinear',random_state=0, C=5, penalty='l2',max_iter=1000)
model=scikit_log_reg.fit(tfidf_train,y_train)


y_pred=pac.predict(tfidf_test)
score=accuracy_score(y_test,y_pred)
print(f'Accuracy: {round(score*100,2)}%')


newdata=pd.read_csv('joebiden.txt')
Xnew=tfidf_vectorizer.transform(newdata["text"])
ynew = model.predict(Xnew) 
for i in range(len(Xnew.toarray() )):
	print("X=%s, Predicted=%s" % (Xnew[i], ynew[i]))
    
print(confusion_matrix(y_test,y_pred, labels=['FAKE','REAL']))
