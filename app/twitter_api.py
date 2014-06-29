import twitter
import nltk
import json
import string
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
        # Search twitter for statuses - ony GET requests available, last 6-9 days of tweets
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
            print json.dumps(status['text'], indent=4) + '\n'

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
        # to see the whole json object with metadata
        # print json.dumps(status_results, indent=4)
        for status in status_results:
            print json.dumps(status['text'], indent=4) + '\n'

    def update_status(self, my_status):
        """
        Updates authenticated users twitter feed by creating new tweet

        @my_status: String
        """
        # Resources regarding Statuses
        # Updates Twitter status (creates a new Tweet) - POST request
        # https://dev.twitter.com/docs/api/1.1/post/statuses/update
        update_status_results = self.twitter_object.statuses.update(
            status=my_status)
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

        tokenized_words = nltk.word_tokenize(
            (corpus.lower()).translate(None, string.punctuation))

        print tokenized_words
        # plot the distribution of the words in a search for #datascience in
        # order they appear in corpus
        nltk.draw.dispersion.dispersion_plot(
            tokenized_words, ['analytics', 'python', 'bigdata', 'machinelearning', 'math', 'stem', 'statistics'])

        # Frequency distribution plot for 50 most frequent words in our corpus
        # (sliced at first 50 words)
        freq_dist_words = nltk.FreqDist(tokenized_words)
        freq_dist_words.plot(50)



# Create instance of class
twitter_api = TwitterApi()
# Methods bound to class twitter_api
twitter_api.search_tweets('#Python', 5)
twitter_api.search_tweets('#javascript', 5)

# gets random 5 tweets from your tweets
twitter_api.search_status(5)

# post a new tweet
twitter_api.update_status("I love Python")

# check you updated status
twitter_api.search_status(1)

twitter_api.plot_status('#datascience', 40)


twitter_api.plot_status('#datascience', 40)

