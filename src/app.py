import os
import requests
import tweepy
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

consumer_key = os.env.get("CONSUMER_KEY")
consumer_secret = os.env.get("CONSUMER_SECRET")
bearer_token = os.env.get("BEARER_TOKEN")


# your app code here
client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret,
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

query = '#100daysofcode (pandas OR python) -is:retweet'

tweets = client.search_recent_tweets(query=query, 
                                    tweet_fields=['author_id','created_at','lang'],
                                     max_results=100)

tweets_dict = tweets.json()                                   

list(tweets_dict)

tweets_data = tweets_dict['data'] 

df = pd.json_normalize(tweets_data)

list(tweets_data[0])