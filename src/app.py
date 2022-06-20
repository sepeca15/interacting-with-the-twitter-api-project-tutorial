import os
import requests
import tweepy
import pandas as pd
import re
import matplotlib.pyplot as plt
import seabron as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

consumer_key = os.env.get("CONSUMER_KEY")
consumer_secret = os.env.get("CONSUMER_SECRET")
bearer_token = os.env.get("BEARER_TOKEN")
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

# your app code here
client = tweepy.Client(bearer_token=bearer_token,
                       consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=os.environ.get('ACCESS_TOKEN'),
                       access_token_secret=os.environ.get(
                           'ACCESS_TOKEN_SECRET'),
                       return_type=requests.Response,
                       wait_on_rate_limit=True)

query = '#100daysofcode (pandas OR python) -is:retweet'

tweets = client.search_recent_tweets(query=query,
                                     tweet_fields=['author_id',
                                                   'created_at', 'lang'],
                                     max_results=100)

tweets_dict = tweets.json()

list(tweets_dict)

tweets_data = tweets_dict['data']

df = pd.json_normalize(tweets_data)

list(tweets_data[0])

df

df.to_csv("coding-tweets.csv")


def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False


[pandas, python] = [0, 0]

for index, row in df.iterrows():
    pandas += word_in_text("pandas", row["text"])
    python += word_in_text("python", row["text"])

sns.set(color_codes=True)

cd = ["pandas", "python"]

ax = sns.barplot(cd, [pandas, python])
ax.set(ylabel="count")
plt.show()
