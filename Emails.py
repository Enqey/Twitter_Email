import tweepy
import re
import time
import pandas as pd


def twitte_auth():
    try:
        consumer_key = ""
        consumer_secret = ""
        access_token = ""
        access_secret = ""

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
    except:
        print('Cant login tweeter.')
    return auth


def get_client():
    auth = twitte_auth()
    client = tweepy.API(auth, wait_on_rate_limit=True)
    return client



client = get_client()
print('Logged In.')

KEY = str(input('[?] Put your email keyword:'))
DELAY = int(input('[?] How many time delay between each scrape:'))
#location = str(input('[?] which location should the mails be from?: '))

textfile = open("emails.txt", "w")

tweets = tweepy.Cursor(client.search, q=KEY,tweet_mode='extended').items()

for status in tweepy.Cursor(client.search, q=KEY, since="2021-05-01").items():
        try:
            match = re.search(r'[\w\.-]+@[\w\.-]+', status.text)
            email = match.group(0)
            username = tweets.user.screen_name
            cols = ['user', 'Email']
            data = []
            data.append([username, email.lower()])
            df = pd.DataFrame(data, columns= cols)
            print(df)
    
#            print(email.lower())
        except:
            continue
    
        try:
            textfile.write(email.lower() + "\n")
        except:
           continue
        time.sleep(DELAY)


#for tweet in tweets:
#    data.append([tweet.user.screen_name, tweet.full_text])
    
#df = pd.DataFrame(data, columns= cols)

#print(df)
        
