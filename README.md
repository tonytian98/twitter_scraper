# twitter_scraper usage:

*twitter_scraper code is in [here](https://github.com/tonytian98/twitter_scraper/blob/main/twitter_scraper.py)*

## Step1: download twitter_scraper.py

## Step2: use python

## Step3: use the code like this, then you will get all the tweets that contain a specific keyword:

```
from twitter_scraper import TweetScraper
scraper=TweetScraper('your_user_name','your_password','keyword',
                      
                      ####below are optional
                      
                      lang = "en"  #language e.g. 'en', 'es', 'ar', 'fr' , 'zh-cn'  (representing english, spanish, Arabic, French, Mandarin) check https://developer.twitter.com/en/docs/twitter-for-websites/supported-languages for details,
                      since=None # when since and until both none, it gets the lastest tweets containing the "keyword" ; but you can also set since = e.g. '2022-04-28',
                      until=None #  The upper time limit of tweets, e.g.  until = '2022-05-28',
                      limit= 2000, #meaning you only get 2000 tweets then the bot stops
                      reply = False, # meaning it won't include reply
                      top = False, # it now gets the lastest tweets from *until* to *start* ; If set to True, it only gets the top (hottest) tweets, notice twitter's top tweets have a limited number, e.g. even if you set *limit*=1000, you may only get 100 top tweets because that's just all of it.
                      hide_bro=True # meaning a browser won't pop up. If it's set to False, a browser will pop up, but you can ignore it, just don't close it!
                      )
data = scraper.scrape()
```
        
The data returned is a list of dictionaries of length limit.

for example:

```
scraper=TweetScraper('user','password','bitcoin',until='2021-01-31',limit= 2)
data = scraper.scrape()
print(data)
```
The result is like:
```
[{'time': '2021-01-31T23:59:03',
  'id': 'JourneyTrade',
  'tweet': 'Beyond Bitcoin: Push For Everyday Cryptocurrency - http://: Beyond Bitcoin: Push For Everyday Cryptocurrency',
  'reply': 0,
  'retweet': 0,
  'like': 0},
 {'time': '2021-01-31T23:59:02',
  'id': 'ZER0fee',
  'tweet': 'New @elonmusk  pattern: #ELONX#Bitcoin #ToTheMoon $DOGE #Tesla #SpaceX #WSB',
  'reply': 0,
  'retweet': 0,
  'like': 1}]
  ```
  
  ### You need to install chrome webdriver and put the file on path(google it), also your python need to have selenium installed 
