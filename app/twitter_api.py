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
# CONSUMER_KEY = ''
# CONSUMER_SECRET = ''
# OAUTH_TOKEN = ''
# OAUTH_TOKEN_SECRET = ''
CONSUMER_KEY = 'C9tTRMqmTi3eAkAEmFx0W92JY'
CONSUMER_SECRET = 'rtukqdLGU8MqWdhVunlS3Wt00J1JcQkxG9pNxDwHxNwZBtJk1s'
OAUTH_TOKEN = '158594198-0kbfhYsQnGnuJDKVSVHaQxSVo5O6UEQGS9uo8FO8'
OAUTH_TOKEN_SECRET = 'CAYid0vCqqLvu34eH5rtHrZdngfGNSBBMix6QQk30uD5Z'

# Classes are used to define state and methods - state keeps track of the
# data and methods do something with that data


class TwitterApi:

    """
    Use the Twitter API to query and update Tweets

    Resource families include: Search and Statuses
    Response is JSON
    """

    def __init__(self):
        """
        Uses Twitter provided tokens to authenticate and connect to twitter API

        Pass in OAuth and consumer tokens to the twitter Oauth class
        and connect as authenticated to the twitter API object
        for queries in search, timelines and tweet resources
        """
        # this is the init dunder method (dunder or 'magic' methods
        # are named for having double underscores)
        # this constructor method gets called when class is instantiated
        # and is where our data gets bound to the instance of the class
        # when its created later
        # the parameter 'self' is a reference to the instance of the
        # TwitterApi class, we also pass it in as a parameter to our
        # methods and is keeping track of our twitter objects state
        # remember we only take care of our application state while
        # the Twitter API takes care of the resource state keeping client
        # and server side separate

        # lets create our twitter object that takes our oauth tokens
        # so we can use our authentication credentials for different
        # resources in the Twitter REST API
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
        # Search twitter for statuses - ony GET requests available, last 6-9
        # days of tweets
        # See https://dev.twitter.com/docs/api/1.1/get/search/tweets

        # Here you can see we pass in self as our first parameter again
        # self now is responsible for any mutation or actions being perfomed on
        # the state

        search_results = self.twitter_object.search.tweets(
            q=search_query, count=count)
        # returns only statuses
        statuses = search_results['statuses']

        for status in statuses:
            if status['retweeted']:
                print "retweeted: ", status['retweeted']
            if status['user']['description']:
                print "user description: ", status['user']['description']
            print json.dumps(status, indent=4) + '\n'

    def search_retweets(self, count):
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

        stopwords = nltk.corpus.stopwords.words('english')

        tokenized_stripped_words = [
            tk for tk in tokenized_words if tk not in stopwords]

        # See the difference between the two tokenized corpi?
        # The first one still has stop words still in the content
        # The second has those words filtered out (such as: 'I', 'me')
        # We will use the filtered list for plotting
        # stopwords and
        print tokenized_words
        print tokenized_stripped_words,  '\n'
        # plot the distribution of the words in a search for #datascience in
        # order they appear in corpus
        nltk.draw.dispersion.dispersion_plot(
            tokenized_stripped_words,
            ['r', 'machine learning', 'nltk', 'hadoop', 'python', 'bigdata', 'big data', 'analytics'])

        # Frequency distribution plot for 50 most frequent words in our corpus
        # (sliced at first 50 words)
        freq_dist_words = nltk.FreqDist(tokenized_stripped_words)
        freq_dist_words.plot(50)

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
twitter_api.search_tweets('#Python', 1)
twitter_api.search_tweets('#javascript', 5)

# gets random 5 tweets from your tweets
twitter_api.search_retweets(5)

# post a new tweet
twitter_api.update_status("I love Python")

# plot query search
twitter_api.plot_status('#datascience', 50)

# search for trends
twitter_api.search_trends(1)
