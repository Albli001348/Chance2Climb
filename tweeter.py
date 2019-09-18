import tweepy

consumer_key ="DdBcMdIRye7yzEXVWfSq2q7nO"
consumer_secret ="cWRaltydOsOR48bdyORuyrMI1w3caYZKKn0MbOLZwsx7KqUX3U"
access_token ="1173753649245245440-TkbWuHxCLR32FGeS2YLnuuP3Ym2CYK"
access_token_secret ="VnDNHANQHIL1O2UHl9Nbka59jlp5ODb9XZXXIpiwknR28"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
   
api = tweepy.API(auth)