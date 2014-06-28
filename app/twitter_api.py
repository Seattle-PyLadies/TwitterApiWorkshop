import twitter
import nltk
import json
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
# CONSUMER_KEY = ''
# CONSUMER_SECRET = ''
# OAUTH_TOKEN = ''
# OAUTH_TOKEN_SECRET = ''
CONSUMER_KEY = 'C9tTRMqmTi3eAkAEmFx0W92JY'
CONSUMER_SECRET = 'rtukqdLGU8MqWdhVunlS3Wt00J1JcQkxG9pNxDwHxNwZBtJk1s'
OAUTH_TOKEN = '158594198-0kbfhYsQnGnuJDKVSVHaQxSVo5O6UEQGS9uo8FO8'
OAUTH_TOKEN_SECRET = 'CAYid0vCqqLvu34eH5rtHrZdngfGNSBBMix6QQk30uD5Z'


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
            # if status['retweeted']:
            #     print "retweeted: ", status['retweeted']
            # if status['user']['description']:
            #     print "user description: ", status['user']['description']
            print json.dumps(status['text'], indent=4)

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
        return status_results

    def update_status(self, my_status):
        """
        Updates authenticated users twitter feed by creating new tweet

        @my_status: String
        """
        # Resources regarding Statuses
        # Updates Twitter status (creates a new Tweet) - POST request
        # https://dev.twitter.com/docs/api/1.1/post/statuses/update
        update_status_results = self.twitter_object.statuses.update(status=my_status)
        return update_status_results

    def plot_status(self, search_query, count):
        """
        Create dispersion plot from search resource filtering by status

        @search_query: hashtag or other string to query
        @count: number of results
        """
        search_results = self.twitter_object.search.tweets(
            q=search_query, count=count)
        statuses = search_results['statuses']

        text_status = []

        for status in statuses:
            # convert unicode to ascii
            encoded_file = status['text'].encode('ascii', 'ignore')
            text_status.append(encoded_file)
        s = ''
        # create proper corpus to tokenize from the various statuses
        corpus = s.join(text_status)

        tokenized_words = nltk.word_tokenize(corpus.lower())
        print tokenized_words
        nltk.draw.dispersion.dispersion_plot(
            tokenized_words, ['analytics', 'python', 'bigdata', 'machinelearning', 'math', 'stem', 'statistics'])

    def search_trends(self, location_id):
        """
        Search for trends

        """
        # Resources regarding Trends
        # Checks for trends based on WOEID, for example global id = 1
        # returns top 10 trends
        # https://dev.twitter.com/docs/api/1.1/get/trends/place
        trends_results = self.twitter_object.trends.place(_id=location_id)
        print json.dumps(trends_results, indent=4)


# Create instance of class
twitter_api = TwitterApi()
# Methods bound to class twitter_api
# twitter_api.search_tweets('#Python', 20)
# twitter_api.search_tweets('#javascript', 20)

# twitter_api.search_status(5)

# twitter_api.update_status("I love Python")

# twitter_api.plot_status('#datascience', 40)

# add curl commands to access tweets
# after POST search status
# add comments about basic programming shit like init
# add trend query OR Friends & Followers
# add one more nltk thingy

twitter_api.search_trends(1)
