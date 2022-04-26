import pandas as pd
import json

def read_json(json_file: str)->list:
    """
    json file reader to open and read json files into a list
    Args:
    -----
    json_file: str - path of a json file
    
    Returns
    -------
    length of the json file and a list of json
    """
    
    tweets_data = []
    for tweets in open(json_file,'r'):
        tweets_data.append(json.loads(tweets))
    
    
    return tweets_data

class TweetExtractor:
    """
    this class extracts tweets it receives in purses them into  a pandas datframe
    """
    def __init__(self, tweetslist):
        
        self.tweetslist = tweetslist


    def find_statuses_count(self)->list:
        """
        finds the status counts for each tweet 
        """
        counts_of_statuses = []
        for tweet in self.tweetslist:
            counts_of_statuses.append(tweet['user']['statuses_count'])
        return counts_of_statuses