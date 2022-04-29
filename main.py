import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pprint import pprint
import string
import os
import re
from extract_data_frame import TweetExtractor,read_json
from clean_tweets_dataframe import CleanTweets
import streamlit as st

# set title
st.title("Twitter Analyzer")

st.sidebar.title("Tweet Modeling")

st.sidebar.subheader("Dataset Specs")


##############
# data specs
#############
tweets_list = read_json("data/Economic_Twitter_Data.json")
tweets_df = TweetExtractor(tweets_list)
tweets_df = tweets_df.get_tweet_df(save=False)
tweets_df.dropna()
if st.sidebar.checkbox("show concise summary"):
    st.write(tweets_df)


#########################
# data preprocessing
#######################
class PrepareData:
  def __init__(self,df):
    self.df=df
    
  def preprocess_data(self):
    tweets_df = self.df.loc[self.df['lang'] =="en"]

    
    #text Preprocessing
    tweets_df['clean_text']=tweets_df['clean_text'].astype(str)
    tweets_df['clean_text'] = tweets_df['clean_text'].apply(lambda x: x.lower())
    tweets_df['clean_text']= tweets_df['clean_text'].apply(lambda x: x.translate(str.maketrans(' ', ' ', string.punctuation)))
    
    #Converting tweets to list of words For feature engineering
    sentence_list = [tweet for tweet in tweets_df['clean_text']]
    word_list = [sent.split() for sent in sentence_list]

    #Create dictionary which contains Id and word 
    word_to_id = corpora.Dictionary(word_list)
    corpus_1= [word_to_id.doc2bow(tweet) for tweet in word_list]

