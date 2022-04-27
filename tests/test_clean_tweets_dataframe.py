import unittest
import pandas as pd
import sys, os
 
sys.path.append(os.path.abspath(os.path.join('../..')))

from clean_tweets_dataframe import CleanTweets

_, tweet_list = read_json("data/covid19.json")

columns = ['created_at', 'source', 'original_text','clean_text', 'sentiment','polarity','subjectivity', 'lang', 'favorite_count', 'retweet_count', 
    'original_author', 'screen_count', 'followers_count','friends_count','possibly_sensitive', 'hashtags', 'user_mentions', 'place', 'place_coord_boundaries']


class TestCleanTweets(unittest.TestCase):
    """
		A class for unit-testing function in the fix_clean_tweets_dataframe.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""
    def setUp(self) -> pd.DataFrame:
        """
        - this function is for the simple setting up of the dataframe
        """
        self.df = pd.read_csv("data/processed_tweet_data.csv")
        self.df_cleanser = CleanTweets(self.df)
    
if __name__ == '__main__':
	unittest.main()

    