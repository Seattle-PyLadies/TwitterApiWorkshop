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
And since we are going to do some fun stuff with our Twitter data, lets install nltk and it's dependencies!
http://www.nltk.org/install.html
```
pip install numpy
pip install pyyaml nltk
pip install matplotlib
```
Lets check our installs:
```
python
import numpy
import nltk
import matplotlib
```
You shouldn't see any errors or any messages if they are correctly installed.
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


