import tkinter
import tweepy

consumer_key = 'LhqACVjssrTqa0skLrw8IrZNm'
consumer_secret = 'QyYxC9ise1x42TjrnRYk9AX4U9uykkD7q3l6Hp9GmiZ1QdfG8z'
access_token = '944871094682398720-Wt9g24cuq0ehuQYcIlrFNMQb3m95qd6'
access_token_secret = 'NxOmaEec9rnp0VHdc8IjbC1POX60nJ4Lp4PNG8Jhtxg2B'
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
