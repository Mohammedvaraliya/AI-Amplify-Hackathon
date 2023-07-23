from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os, sys, gc, warnings
import logging, math, re, heapq
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter    
from nltk.tokenize import word_tokenize
from nltk.corpus import words
import spacy


# This is to download stop words for cleaning the tweets
import nltk



class AutoCorrect:
    def __init__(self) -> None:
        nltk.download('words')
        self.word_list = words.words()
        self.vocab = set(words.words())
        self.word_count_dict = Counter(self.word_list)


        self.probs = {} 
        self.total_words = sum(self.word_count_dict.values())

        for word, word_count in self.word_count_dict.items():
            word_prob = word_count/self.total_words
            self.probs[word] = word_prob

        nlp = spacy.load('en_core_web_sm')
        doc = nlp("I live in New York and work as a data scientist.")
        for word in doc.ents:
            print(word.text, word.label_)

    def delete_letter(self, word):
        delete_list = []
        split_list = []
        split_list = [(word[:i], word[i:]) for i in range(len(word))]
        delete_list = [L+R[1:] for L, R in split_list]
        return delete_list

    def switch_letter(self, word):
        switch_list = []
        split_list = []
        split_list = [(word[:i], word[i:]) for i in range(len(word))]
        switch_list = [L + R[1] + R[0] + R[2:] for L, R in split_list if len(R)>=2]
        return switch_list

    def replace_letter(self, word):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        replace_list = []
        split_list = []
        split_list = [(word[0:i], word[i:]) for i in range(len(word))]
        replace_list = [L + letter + (R[1:] if len(R)>1 else '') for L, R in split_list if R for letter in letters]
        replace_set = set(replace_list)
        replace_list = sorted(list(replace_set))   
        return replace_list

    def insert_letter(self, word):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        insert_list = []
        split_list = []
        split_list = [(word[0:i], word[i:]) for i in range(len(word)+1)]
        insert_list = [L + letter + R for L, R in split_list for letter in letters]
        return insert_list

    def edit_one_letter(self, word, allow_switches = True):
        edit_one_set = set()
        edit_one_set.update(self.delete_letter(word))
        if allow_switches: edit_one_set.update(self.switch_letter(word))
        edit_one_set.update(self.replace_letter(word))
        edit_one_set.update(self.insert_letter(word))
        if word in edit_one_set: edit_one_set.remove(word)
        return edit_one_set

    def edit_two_letter(self, word, allow_switches = True):
        edit_two_set = set()
        edit_one = self.edit_one_letter(word, allow_switches=allow_switches)
        for word in edit_one:
            if word:
                edit_two = self.dit_one_letter(word, all,  ow_switches=allow_switches)
                edit_two_set.update(edit_two)
        
        return edit_two_set
    
    def get_spelling_suggestions(self, word):    
        suggestions = []
        top_n_suggestions = []
        suggestions = list((word in self.vocab and word) or 
                        self.edit_one_letter(word).intersection(self.vocab) or
                        self.edit_two_letter(word).intersection(self.vocab))
        top_n_suggestions = [[s, self.probs[s]] for s in list(suggestions)]
        return top_n_suggestions

app = Flask(__name__)
at = AutoCorrect()
CORS(app)  # Enable CORS for the entire app

# Your app routes and other code go here...

# Enable CORS for a specific endpoint using the CORS decorator
@app.route('/', methods=['GET', 'POST'])
# @CORS(app, resources={r"/": {"origins": "http://localhost:3000/"}})
def specific_endpoint():
    if request.method == "POST":
        word = request.json["word"]

        suggestions = at.get_spelling_suggestions(word)
        return jsonify({"suggestions" : suggestions})
    elif request.method == "GET":
        data = {'message': 'This is a specific endpoint.'}
        return jsonify(data)
    else:
         return jsonify({'message': 'Unsupported method.'}), 405

if __name__ == '__main__':
    app.run(debug=True)
