# get_tweets.py

import sys
import json
from twarc import Twarc2, expansions
from configparser import ConfigParser

#TWARC CONFIG
TWARC_CONFIG_FILE = "################"
OUTPUT_FILE = str(sys.argv[1]) + '.jsonl'   # line-oriented JSON
MAX_TWEETS = 60

# read Twitter API keys from twarc config file, setup twarc2 object
config = ConfigParser(interpolation=None)
with open(TWARC_CONFIG_FILE) as twarc_config:
     config.read_string("[TWARC]\n" + twarc_config.read())
bearer_token = config['TWARC']['bearer_token'].strip('\'')
t = Twarc2(bearer_token=bearer_token)

# use nothing as default search term unless one provided which should always be the case
search_term = " "
if len(sys.argv) > 1:
     search_term = str(sys.argv[1])
else:
     raise Exception('please provide a search term') #we don't want to search for nothing

# limit search results to English language not a link (trying to handle spam) no retweets
query = search_term + " lang:en -has:links -is:retweet"

#get results
search_results = t.search_recent(query=query, max_results=MAX_TWEETS)

num_tweets = 0
for page in search_results:
     # The Twitter API v2 returns the Tweet information and the user, media, etc. separately
     # so we use expansions.flatten to get all the information in a single JSON
     result = expansions.flatten(page)
   
     # open the file and write one JSON object per new line (jsonl format)
     with open(OUTPUT_FILE, 'a+') as filehandle:  
          for tweet in result:
               filehandle.write('%s\n' % json.dumps(tweet))
               num_tweets = num_tweets + 1
               if num_tweets == MAX_TWEETS:
                    # must include this to stop after a certain # of tweets
                    search_results.close()

print (num_tweets, "tweets written to " + OUTPUT_FILE + " for query \"" + query + "\"\n");

