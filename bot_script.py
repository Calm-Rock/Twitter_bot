import tkinter
import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)


for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print ("Followed everyone that is following " + user.name)

def mainFunction():
    search = "Flask"
    numberOfTweets = 5
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.favorite()
            print('<3 the tweet')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
        
    tweetId = tweet.user.id
    username = tweet.user.screen_name

    phrase = "Flask is Awesome!"
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweetId = tweet.user.id
            username = tweet.user.screen_name
            api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
            print ("Replied with " + phrase)
            print(tweetId)
            print(username)
            
        except tweepy.TweepError as e:   
             print(e.reason)
        except StopIteration:
            break

mainFunction()
