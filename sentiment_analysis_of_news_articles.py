# -*- coding: utf-8 -*-
"""Sentiment Analysis of News Articles

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yCmLd_F1gtx6D-TX8WMFX81vuKxdM09J
"""

# Commented out IPython magic to ensure Python compatibility.
# !pip install bs4
# !pip install TextBlob
# !pip install pattern
# !pip install tqdm
# !pip install ipython-autotime
# %load_ext autotime
from bs4 import BeautifulSoup
import requests 
import numpy as np
import pandas as pd
from textblob import TextBlob
from pattern.en import sentiment
from tqdm import tqdm
import json



#websraping
content = requests.get('https://www.aljazeera.com/where/mozambique/')
soup = BeautifulSoup(content.content, 'html.parser')
#print(soup)

#pre-processing the data

n=0

textblob_sentiment=[]
pos=0
neg=0
neu=0

val=[]

for i in tqdm(range(100), desc = 'tqdm() Progress Bar'):
  for foo in soup.find_all('div', attrs={'class': 'gc__excerpt'}):
        for s in foo.find('p'):
          print(s)
          txt= TextBlob(s)
          a= txt.sentiment.polarity
          b= txt.sentiment.subjectivity
          if a > 0:
              sentiment="positive"
              if(n<10):
                pos+=1
          elif a == 0:
              sentiment="neutral"
              if(n<10):
                neu+=1
          else:
              sentiment="negative"
              if(n<10):
                neg+=1
          n+=1
          textblob_sentiment.append([s,a,b,sentiment])
          s=s.replace('\u2019','')
          val.append(s.replace('\u00ad',''))

text=textblob_sentiment[0:10]
val1=val[0:10]

import json
  
# python object(dictionary) to be dumped
dict1 = {} 
# Adding list as value
dict1["News articles"] = val1
# the json file where the output must be stored
file = open("news.json", "w")
json.dump(dict1, file, indent = 6)
file.close()

df_textblob = pd.DataFrame(text, columns =['Sentence', 'Polarity', 'Subjectivity','Sentiment'])


df_textblob.tail(10)

import plotly.graph_objects as go

fig1 = go.Figure(
    data=[go.Bar(x=[i for i in range(1, 11)], y=df_textblob["Polarity"])],
    layout_title_text="Sentence Polarity - Positive(>0), Negative(<0), Neutral(=0)"
)
fig1.show()

fig2 = go.Figure(
    data=[go.Bar(y=df_textblob["Subjectivity"])],
    layout_title_text="Sentence Subjectivity"
)
fig2.show()

fig3 = go.Figure(
    data=[go.Bar(x=["Positive", "Neutral", "Negative"], y=[pos, neu, neg])],
    layout_title_text="Sentiment of news articles"
)
fig3.show()

#alternative approach using vaderSentiment

#!pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

senti=[]

for i in tqdm(range(100), desc = 'tqdm() Progress Bar'):
  for foo in soup.find_all('div', attrs={'class': 'gc__excerpt'}):
      for s in foo.find('p'):
        print(s)
        analyzer = SentimentIntensityAnalyzer() 
        vs = analyzer.polarity_scores(s)
        print("{:-<65} {}".format(s, str(vs)))
        s=s.replace('\u2019','')
        s=s.replace('\u00ad','')
        senti.append([s, str(vs)])
        
senti=senti[0:10]

for i in range(10):
  print(senti[i])

