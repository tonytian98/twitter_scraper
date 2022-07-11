# twitter_scraper usage:

*twitter_scraper code is in [here]()*

download twitter_scraper.py

use python script or jupyternotebook

use the code like this:

```
scraper=TweetScraper('your_user_name','your_password','keyword',
                      
                      ####below are optional
                      
                      lang = "en"  #language e.g. 'en', 'es', 'ar', 'fr' , 'zh-cn'  (representing english, spanish, Arabic, French, Mandarin) check                    https://developer.twitter.com/en/docs/twitter-for-websites/supported-languages for details,
                      since=None # when since and until both none, it gets the lastest tweets containing the "keyword"  but e.g. you can set since ='2022-04-28',
                      until=None #  The upper time limit of tweets, e.g.  until = '2022-05-28',
                      limit= 2000, #meaning you only get 2000 tweets then the bot stops
                      reply = False, # meaning it won't include reply
                      hide_bro=True # meaning a browser won't pop up. If set to FALSE it will.
                      )
data = scraper.scrape()
```
        
The data returned is dictionaries in a list of length limit.\

for example:

```
scraper=TweetScraper('user','password','bitcoin',until=f'2021-01-31',limit= 2)
data = scraper.scrape()
print(data)
```
The result is like:
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
