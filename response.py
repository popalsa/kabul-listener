# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '302168391-glkmuC0G5gTvc23s91qP1a3pFda0diLvpRKflR4f'
ACCESS_SECRET = 'Dj2Q4sI8hfK3bMJtvA7J4j6hZ4yO3O8hCcyHRletriSGi'
CONSUMER_KEY = 'l5J8RI7xG8cCUgOUFTSrP8p20'
CONSUMER_SECRET = 'ydQyFlU8l56K7i3hNBzPvYRYVznI8stE2ALzhSiIyQ3c6durpn'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

t = Twitter(auth=oauth)

t.statuses.update(status="I think @chalkley_larry smells")