import twitter

# API and OAuth creds

"""
Now that we have our set up all taken
care of, lets get our access tokens
from Twitter.
https://dev.twitter.com/docs/auth/obtaining-access-tokens
All we need is to use testing tokens
https://dev.twitter.com/docs/auth/tokens-devtwittercom
"""
# Global auth vars
CONSUMER_KEY = ''
CONSUMER_SECRET =''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

class Twitter_Api:

    def __init__(self):
        self.auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
        # create twitter object
        self.twitter_object = twitter.Twitter(auth=self.auth)

    def search_tweets(self, search_query, count):
        """
        Search twitter for statuses - ony GET requests available
        @search_query: hashtag you want see statuses of.
        @count: limit of returned statuses
        """
        # See https://dev.twitter.com/docs/api/1.1/get/search/tweets
        search_results = self.twitter_object.search.tweets(q=search_query, count=count)
        # returns only statuses
        statuses = search_results['statuses']

        for status in statuses:
            print "status text : ", status['text']
            if status['retweeted']:
                print "retweeted: ", status['retweeted']
            print "user description: ", status['user']['description']

            return status

    def search_status(self, twitter_id, count):
        """
        To retrieve retweets of your Tweets
        https://dev.twitter.com/docs/api/1.1/get/statuses/retweets_of_me
        To get your Twitter Id
        http://www.idfromuser.com/
        """
        status_results = self.twitter_object.statuses.retweets_of_me(since_id=twitter_id, count=count)
        print status_results


twitter_api = Twitter_Api()
twitter_api.search_tweets('#RaspberryPi', 5)
twitter_api.search_tweets('RaspberryPi', 5)

twitter_api.search_status('158594198', 5)