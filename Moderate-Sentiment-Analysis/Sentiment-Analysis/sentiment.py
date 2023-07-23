from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request

# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
 
 
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

def calculatesentiment(text):
    task='sentiment'
    MODEL = f"cardiffnlp/twitter-roberta-base-{task}"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    labels=[]
    mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
    with urllib.request.urlopen(mapping_link) as f:
        html = f.read().decode('utf-8').split("\n")
        csvreader = csv.reader(html, delimiter='\t')
        labels = [row[1] for row in csvreader if len(row) > 1]
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    model.save_pretrained("sentiment_model")
    tokenizer.save_pretrained("tokenizer")
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    result = {}
    for i in range(scores.shape[0]):
        l = labels[ranking[i]]
        s = scores[ranking[i]]

        result[l] = s
        print(f"{i+1}) {l} {np.round(float(s), 4)}")
    return result
    

A = calculatesentiment("This is 19 year old Aditya Prabhu who was studying CSE at PES, Bangalore. On July 17th, he jumped from the 8th floor of a building in the campus and killed himself. What drove him to such extreme step? Aditya was allegedly caught copying in a college exam. The college authorities rounded him up and called his mother to the campus. Unable to bear the humiliation of facing his mom in front of the college authorities, he decided to commit suicide. The college tried to wash their hands off by going to the media and declaring that Aditya was caught copying. The mother has gone to social media seeking justice for her son. Social media users are popularising the hashtag #justiceforadityaprabhu. They will move on to the next hashtag after a few days. I look at the boy’s face and it breaks my heart. I consider him to be a unlucky boy - because he was born with an above average intelligence and sensitive heart in a country like India. He did not commit suicide. The system of societal expectations, extreme performance pressure, exam oriented approach to learning, and a band of soulless educators trying to monetise the education system - they collectively killed him. On ChatGPT and free coding websites like CodeAcademy, all knowledge is freely available to the world. In such times, we are conducting written exams to test the memorisation power of students. It is beyond ridiculous. We want everything latest - smartphones, music system, TVs, shoes, refrigerators - but we are okay to settle with an education system that has remained unchanged for 100 years. It is disappointing and sad. There is something seriously wrong with us as a nation.")
print("A is: ",A)
