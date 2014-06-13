#Welcome to the Seattle PyLadies Twitter API tutorial
Lets get started by creating our project and setting up our environment
First create a directory:
```
mkdir twitter_api_tutorial
cd twitter_api_tutorial
```
Then we'll create and activate our virtual environment
```
virtualenv -p python2.7 tut_env
source tut_env/bin/activate
```
Now download the Twitter library
```
pip install twitter
```
And create a requirements.txt file so we can keep track of our installed libraries!
```
pip freeze > requirements.txt
```
Now create another directory called app which will hold, you guessed it - our app!
```
mkdir app
cd app
touch twitter_api.py
```

Now that we have our set up all taken
care of, lets get our access tokens
from Twitter.
https://dev.twitter.com/docs/auth/obtaining-access-tokens
All we need is to use the dev auth tokens and the
https://dev.twitter.com/docs/auth/tokens-devtwittercom
