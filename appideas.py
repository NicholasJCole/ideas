# need to create a database
# run this program every n minutes and add tweets to db
# pull last n tweets from db and paginate or make never ending
# wall of tweets

# great sqlite3 tutorial
# http://www.pythoncentral.io/introduction-to-sqlite-in-python/



from twitter import Twitter, OAuth, TwitterHTTPError
import twitterapidetails as tad
import sqlite3

# db should contain:
# tweet id, tweet profile name, tweet prof image link, tweet content, tweet date


db = sqlite3.connect('tweetdata')
cursor = db.cursor()
#cursor.execute('''CREATE TABLE tweets(id TEXT, profname TEXT, screenname TEXT, profimagelink TEXT, tweetcontent TEXT, tweetdate TEXT)''')



db.commit()



t = Twitter(auth=OAuth(tad.OAUTH_TOKEN, tad.OAUTH_SECRET,tad.CONSUMER_KEY, tad.CONSUMER_SECRET))

def search_tweets(q, count=100):
    return t.search.tweets(q=q, result_type='recent', count=count)
    
    
results = search_tweets('"There should be an app"')


# parts of tweet that are of interest:
# under results['statuses'][0]:
# 'text', 'profile_image_url_https', 'id' <-- id of tweet

# under results['statuses'][0]['user']:
# ['name'] # actual name, not twitter name
# ['screen_name']
# ['profile_image_url']

for status in results['statuses']:
    # get rid of RTs
    if "RT" not in status['text']:
        tweet_id = status['id']
        tweet_content = status['text']
        tweet_prof_image = status['user']['profile_image_url']
        tweet_prof_name = status['user']['screen_name']
        tweet_actual_name = status['user']['name']
        tweet_create_time = status['created_at']
        #print tweet_content
        cursor.execute('''INSERT INTO tweets(id, profname, screenname, profimagelink, tweetcontent, tweetdate) 
            VALUES (?,?,?,?,?,?)''', (tweet_id, tweet_prof_name, tweet_actual_name, tweet_prof_image, tweet_content, tweet_create_time))
    # add to db
    # db should contain:
    # tweet id, tweet profile name, tweet prof image link, tweet content, tweet
db.commit()    

for status in ai.results['statuses']:
    # get rid of RTs
    if "RT" not in status['text']:
        tweet_id = status['id']
        tweet_content = status['text']
        tweet_prof_image = status['user']['profile_image_url']
        tweet_prof_name = status['user']['screen_name']
        tweet_actual_name = status['user']['name']
        tweet_create_time = status['created_at']
        # check to see if in tweet_id in database, if not then put in
        cursor.execute('''INSERT INTO tweets(id, profname, screenname, profimagelink, tweetcontent, tweetdate) 
            VALUES (?,?,?,?,?,?)''', (tweet_id, tweet_prof_name, tweet_actual_name, tweet_prof_image, tweet_content, tweet_create_time))
  



