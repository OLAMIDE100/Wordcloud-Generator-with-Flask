import snscrape.modules.twitter as sntwitter
import pandas as pd
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from PIL import Image
from io import StringIO
from flask import send_file




def get_tweets(maxTweets,trend,startdate,enddate):
    maxTweets = maxTweets
    input = '%s since:%s until:%s'%(trend,startdate,enddate)

    tweets_list2 = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(input).get_items()):
        if i>maxTweets:
            break
        tweets_list2.append([tweet.content])
    
    tweets = pd.DataFrame(tweets_list2, columns=['Text'])
    
    def processed_tweet(tweet):
        return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ', tweet).split())
    
    tweets['processed_tweet'] = tweets['Text'].apply(lambda x: processed_tweet(x))
    
    all_tweets = ' '.join(tweet for tweet in tweets['processed_tweet'])
    
    
    wordcloud = WordCloud(stopwords=STOPWORDS,background_color="black").generate(all_tweets)
    image = wordcloud.to_image()
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())

    return img_str.decode('utf-8')
    
