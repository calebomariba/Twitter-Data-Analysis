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

