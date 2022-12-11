""""
Title: Assignment 5.1-2 Horoscope Classification 
Author: Simone Lewis
with scikit-learn
Date: 12-05-2022


This script contains the solutions for problems 1-2 from assignment 5. 
"""""

#dependencies and libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


data = pd.read_csv('horoscopes.csv')
#reading CSV file
corpus = data['horoscope']
cv = CountVectorizer(max_df=0.9, min_df=5, stop_words='english')
#preprocessing horoscopes
idxs0 = data['sign'] == 'virgo'
idxs1 = data['sign'] == 'scorpio'
idxs = idxs0.values + idxs1.values
#extracts the predictors to become X
corpus = corpus[idxs]
X = cv.fit_transform(corpus.values).toarray()
y = data['sign'].loc[idxs].values

X_train, X_test, y_train, y_test = train_test_split(
#split array into train and test subjects
    X,
    y,
    test_size=0.23,
    random_state=23
    )

classifier = MultinomialNB()
classifier.fit(X_train , y_train)
#classification matrix 

y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
#returns number of correct and incorrext predictions
print(f'Approximate Accuracy: {accuracy_score(y_test, y_pred)}')
print(f'Accuracy in cases: {accuracy_score(y_test, y_pred, normalize=False)}')


"""""
Performance of the classifier isn't very good.
It has an accuracy perceptage of 55% without 
preprocessing  for stop-words.

An accuracy value of 275 is returned. 

When preprocessing for stop-words, it returns 
an accuracy percentage of 53%. 

The confusion matrix returns high values for the false
positive and false negative, meaning that the model 
innacurately classified these classes a high number of times, 
which isn't acceptable. 
"""""