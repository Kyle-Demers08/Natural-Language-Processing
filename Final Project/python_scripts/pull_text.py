import sys
import json
from datetime import datetime

# read in lines of JSON from stdin
lines = sys.stdin.readlines()  # read in all the lines

txt = []
#this is used with jsonl which is one object per line
for line in lines:
    tweet_data = json.loads(line)  # each object is JSON
    text = tweet_data['text']  # Get the actual text tweeted
    if text in txt: #no repeats
        continue
    txt.append(text)

print(txt)

