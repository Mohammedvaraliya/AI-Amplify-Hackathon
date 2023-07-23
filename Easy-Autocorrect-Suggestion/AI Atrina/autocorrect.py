# Import the libraries for processing data and other utilities

import streamlit as st
import nltk
import spacy
from nltk.corpus import words
from collections import Counter
import os, sys, gc, warnings
import logging, math, re, heapq
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter    
from nltk.tokenize import word_tokenize
from nltk.corpus import words

# This is to download stop words for cleaning the tweets
import nltk
nltk.download('words')

word_list = words.words()
vocab = set(words.words())

# Initiating the word_count dictionary and populating it
word_count_dict = {}
word_count_dict = Counter(word_list)
print(f"There are {len(word_count_dict)} key values pairs")
print(f"The count for the word 'thee' is {word_count_dict.get('thee',0)}")

# Initalize the probability dictionary
probs = {} 
total_words = sum(word_count_dict.values())

for word, word_count in word_count_dict.items():
    word_prob = word_count/total_words
    probs[word] = word_prob
print(f"Length of probs is {len(probs)}")

# Let us use both the dictionaries for both word counts and probabilities and display an example word.
print(f"P('thee') is {probs['thee']:.4f}")
print(word_count_dict['thee'])

import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("I live in New York and work as a data scientist.")
for word in doc.ents:
    print(word.text, word.label_)


def delete_letter(word):
    delete_list = []
    split_list = []
    split_list = [(word[:i], word[i:]) for i in range(len(word))]
    delete_list = [L+R[1:] for L, R in split_list]
    return delete_list

def switch_letter(word):
    switch_list = []
    split_list = []
    split_list = [(word[:i], word[i:]) for i in range(len(word))]
    switch_list = [L + R[1] + R[0] + R[2:] for L, R in split_list if len(R)>=2]
    return switch_list

def replace_letter(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    replace_list = []
    split_list = []
    split_list = [(word[0:i], word[i:]) for i in range(len(word))]
    replace_list = [L + letter + (R[1:] if len(R)>1 else '') for L, R in split_list if R for letter in letters]
    replace_set = set(replace_list)
    replace_list = sorted(list(replace_set))   
    return replace_list

def insert_letter(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    insert_list = []
    split_list = []
    split_list = [(word[0:i], word[i:]) for i in range(len(word)+1)]
    insert_list = [L + letter + R for L, R in split_list for letter in letters]
    return insert_list

def edit_one_letter(word, allow_switches = True):
    edit_one_set = set()
    edit_one_set.update(delete_letter(word))
    if allow_switches: edit_one_set.update(switch_letter(word))
    edit_one_set.update(replace_letter(word))
    edit_one_set.update(insert_letter(word))
    if word in edit_one_set: edit_one_set.remove(word)
    return edit_one_set

def edit_two_letter(word, allow_switches = True):
    edit_two_set = set()
    edit_one = edit_one_letter(word, allow_switches=allow_switches)
    for word in edit_one:
        if word:
            edit_two = edit_one_letter(word, allow_switches=allow_switches)
            edit_two_set.update(edit_two)
    
    return edit_two_set


def get_spelling_suggestions(word, probs, vocab, n=2,):    
    suggestions = []
    top_n_suggestions = []
    suggestions = list((word in vocab and word) or 
                       edit_one_letter(word).intersection(vocab) or
                       edit_two_letter(word).intersection(vocab))
    top_n_suggestions = [[s, probs[s]] for s in list(suggestions)]
    return top_n_suggestions

my_words = ['sectin','condtion','condotin','disdaain','tumtultous']
tmp_corrections = []
for word_c in my_words:
    tmp_corrections.append(get_spelling_suggestions(word_c, probs, vocab, 3))
for i, word in enumerate(my_words):
    print(' ')
    print(f'Word - {my_words[i]}')
    for j, word_prob in enumerate(tmp_corrections[i]):
        print(f"word - {j}: {word_prob[0]}, probability {word_prob[1]:.6f}")

word = ""

def main():
    st.title("Spelling Suggestions")

    # User input
    user_input = st.text_input("Enter a word:", value=word, key="user_input")

    if user_input:
        # Get spelling suggestions
        suggestions = get_spelling_suggestions(user_input.lower(), probs, vocab, n=3)

        st.write(f"Spelling suggestions for '{user_input}':")
        for i, (suggestion, probability) in enumerate(suggestions):
            # Create a button for each suggestion
            if len(suggestion) > 1:
                if st.button(suggestion):
                    # Set the text input value to the selected suggestion
                    user_input = user_input.capitalize()


if __name__ == "__main__":
    main()