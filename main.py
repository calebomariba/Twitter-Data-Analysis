import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import STOPWORDS,WordCloud
import gensim
from gensim.models import CoherenceModel
from gensim import corpora
import pandas as pd
from pprint import pprint
import string
import os
import re
from extract_dataframe import ExtractTweets
from clean_tweets_dataframe import TweetCleanser

# set title
st.title("Twitter Analyzer")

st.sidebar.title("Tweet Modeling")

st.sidebar.subheader("Dataset Specs")


##############
# data specs
#############
tweets_df = ExtractTweets("data/Economic_Twitter_Data.json")
tweets_df = tweets_df.get_tweet_df(save=False)
tweets_df.dropna()
if st.sidebar.checkbox("show concise summary"):
    st.write(tweets_df)

