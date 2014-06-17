import twitter

# API and OAuth creds

"""
Now that we have our set up all taken
care of, lets get our access tokens
from Twitter.
https://dev.twitter.com/docs/auth/obtaining-access-tokens
All we need is to use testing tokens
https://dev.twitter.com/docs/auth/tokens-devtwittercom
Under Application settings under Access Level: Read, write, and direct messages
If you want to have write access then you now have to go to your Twitter profile
Then enable mobile (I have all notifactions unchecked)
"""
# Global auth vars
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''


class TwitterApi:
    """
    Use the Twitter API to query and update Tweets

    Resource families include: Search and Statuses
    Response is JSON
    """

    def __init__(self):
        """
        Uses Twitter provided tokens to authenticate and connect to twitter API

        Pass in OAuth and consumer tokens to twitter Oauth class
        and connect as authenticated to the twitter API object
        for queries in search, timelines and tweet resources
        """
        # constructor method gets called when class is instantiated
        # we create our twitter object that takes our oauth tokens
        # so we can use our auth credentials in different resources
        # from the Twitter REST API
        self.auth = twitter.oauth.OAuth(
            OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
        self.twitter_object = twitter.Twitter(auth=self.auth)

    def search_tweets(self, search_query, count):
        """
        Queries Twitters search resource for statuses by keyword or hashtag

        @search_query: hashtag you want see statuses of.
        @count: limit of returned statuses
        """
        # Resources regarding Search
        # Search twitter for statuses - ony GET requests available
        # See https://dev.twitter.com/docs/api/1.1/get/search/tweets
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
        Queries Twitter timeline statuses resource of consumer token related retweets

        @count: limit of returned statuses
        """
        # Resources regarding Statuses
        # To retrieve retweets of your Tweets - GET request
        # https://dev.twitter.com/docs/api/1.1/get/statuses/se
        status_results = self.twitter_object.statuses.retweets_of_me(
            count=count)
        print status_results

    def update_status(self, my_status):
        """
        Updates authenticated users twitter feed by creating new tweet

        @status:
        """
        # Resources regarding Statuses
        # Updates Twitter status (creates a new Tweet) - POST request
        # https://dev.twitter.com/docs/api/1.1/post/statuses/update
        update_status = self.twitter_object.statuses.update(status=my_status)
        return update_status

# Create instance of class
twitter_api = TwitterApi()
# Methods bound to class twitter_api
twitter_api.search_tweets('#RaspberryPi', 5)
twitter_api.search_tweets('RaspberryPi', 5)
twitter_api.search_status(5)
twitter_api.update_status("I love Python")
