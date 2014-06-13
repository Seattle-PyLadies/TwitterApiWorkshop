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
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''


class TwitterApi:

    def __init__(self):
        """
        constructor method gets called when class is instantiated
        we create our twitter object that takes our oauth tokens
        so we can use our auth credentials in different resources
        the Twitter REST API
        """
        self.auth = twitter.oauth.OAuth(
            OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
        self.twitter_object = twitter.Twitter(auth=self.auth)

    def search_tweets(self, search_query, count):
        """
        Search twitter for statuses - ony GET requests available
        See https://dev.twitter.com/docs/api/1.1/get/search/tweets
        @search_query: hashtag you want see statuses of.
        @count: limit of returned statuses
        """
        search_results = self.twitter_object.search.tweets(
            q=search_query, count=count)
        # returns only statuses
        statuses = search_results['statuses']

        for status in statuses:
            print "status text : ", status['text']
            if status['retweeted']:
                print "retweeted: ", status['retweeted']
            print "user description: ", status['user']['description']
            return status

    def search_status(self, count):
        """
        To retrieve retweets of your Tweets
        https://dev.twitter.com/docs/api/1.1/get/statuses/se
        """
        status_results = self.twitter_object.statuses.retweets_of_me(
            count=count)
        print status_results

# Create instance of class
twitter_api = TwitterApi()
# Methods bound to class twitter_api
twitter_api.search_tweets('#RaspberryPi', 5)
twitter_api.search_tweets('RaspberryPi', 5)
twitter_api.search_status(5)
