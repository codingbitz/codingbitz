from flask import Flask, render_template, url_for, request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def spamham_predict():
	
    NB_spam_model = open('spam-nb-model.pkl','rb')
    clf = joblib.load(NB_spam_model)
    
    cv_model = open('count_vect.pkl', 'rb')
    cv = joblib.load(cv_model)
    
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        predict_spha = clf.predict(vect)
	
    return render_template('result.html',prediction = predict_spha)


if __name__ == '__main__':
	app.run()