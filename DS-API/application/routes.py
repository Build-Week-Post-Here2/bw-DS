from flask import request, jsonify, render_template
from flask import current_app as app
import numpy as np 
import pandas as pd 
import json
import pickle
from flask_cors import CORS

# Allow for Cross Origin Resource Sharing
CORS(app)

# pickled vectorizer and classifier
with open('vectorizer2.pkl', 'rb') as file:
    vec_pickle = pickle.load(file)

with open('SGDClassifier_pickle.pkl', 'rb') as file1:
    clf_pickle = pickle.load(file1)

# endpoint for sending the post    
@app.route('/predict', methods=['POST'])
def make_predict():
    # read in data
    text_inputs = request.get_json(force=True)
    
    # get variables
    title = text_inputs['title']
    selftext = text_inputs['body']
    
    # combine
    text = title + ' ' + selftext

    # vect should be pickled here, make the text into a list
    text_vect = vec_pickle.transform([text])
    
    # make prediction USING PICKLED MODEL 
    output = clf_pickle.predict(text_vect)

    # send back the top subreddit

    return jsonify(prediction = output[0])


@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')