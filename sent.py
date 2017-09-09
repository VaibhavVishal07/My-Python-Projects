import tweepy
from textblob import TextBlob

consumer_key='3Szz8WEew0TjxCUgksaJXfh7G'
consumer_secret='zquiubR1q1lgjAEizByXEJw7aSGTAtziRW08QqaZDPdvXHX0J8'

access_token='524376269-S24KUnGwxnTH8fXPAhouLBTy61vLFbjnfKPkUqGl'
access_token_secret='kUC4J7Gw4gJTue6FfIwI2Empp3t7yCODnVAAp6kPsEDNM'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

print "On what topic do you want to know the sensitivity?"
public_tweets=api.search(raw_input(""))

for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)

