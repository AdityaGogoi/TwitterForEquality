TRACK_TERMS = ["trump", "clinton", "sanders", "hillary clinton", "bernie", "donald trump"]
TWITTER_APP_KEY = 'L9vlGbzWDyKKISKM7ckkiqM6R'
TWITTER_APP_SECRET = 'QcU4U93yaoeRGzYw5E9a1DZMPb16PH0cy0JZlSbVAolf0RvR45' 
TWITTER_KEY = '2256521072-9isKVKR9p06qVGtm71ODwEJguufF6hx3VK5EhyN'
TWITTER_SECRET = 'XvJPjbot8aJAouu33jLK27e6vzkP2L5TNjBTYcN2m0ZWj'
CONNECTION_STRING = 'sqlite:///tweets.db'
CSV_NAME = "tweets.csv"
TABLE_NAME = "election"

try:
    from private import *
except Exception:
    pass