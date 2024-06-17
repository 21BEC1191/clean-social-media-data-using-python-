from collections import Counter
import tweepy
import matplotlib.pyplot as plt
from textblob import TextBlob

consumer_key = 'sWXu5Hwm0kr0aTjugLpxhzSs1'
consumer_secret = 'fz4Wls6rjIqD5iPT31GGty2h51IWNhmaeVqCZ4DhB3wmntEef0'
access_token = '1802539018673922048-f3sqF4nlxPaQAO3CseWERoLlmwUZPs'
access_token_secret = 'rGDIfl0QMq2nrzRSOGOEeunUUqFCGaLLMtVKgvOk4EvvU'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search_tweets, q='query', lang='en', tweet_mode='extended').items(1000)


# Analyzing Sentiment and Counting Words
word_freq = Counter()
sentiments = []
for tweet in tweets:
    text = tweet.full_text
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    sentiments.append(sentiment)
    words = text.split()
    word_freq.update(words)

# Visualizing Top 10 Most Common Words
top_words = word_freq.most_common(10)
labels = [x[0] for x in top_words]
counts = [x[1] for x in top_words]
plt.bar(labels, counts)
plt.title("Top 10 Most Common Words in Tweets")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.show()

# Displaying Sentiments
for i, tweet in enumerate(tweets):
    print(f"Tweet {i+1}: {tweet.full_text}")
    print("Sentiment:", sentiments[i])