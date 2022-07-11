
from time import sleep
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class TweetScraper():
    def __init__(self,user_name, password, keyword, lang='en',since=None, until = None, top = False, limit=2000, reply = False, hide_bro=False):
        self.limit = limit
        self.error_count=0
        self.hide_bro = hide_bro
        self.user_name = user_name
        self.password = password
        if top == True:
            self.type = ''
        else:
            self.type = '&f=live'

        if reply:
            self.filter = ''
        else:
            self.filter='-filter%3Areplies'

        if since==None and until == None:
            self.src=f'https://twitter.com/search?lang=en&q={keyword}%20lang%3A{lang}%20{self.filter}&src=typed_query{self.type}'

        elif since and until:
            self.src= f'https://twitter.com/search?lang=en&q={keyword}%20lang%3A{lang}%20until%3A{until}%20since%3A{since}%20{self.filter}&src=typed_query{self.type}'
        elif since:
            self.src= f'https://twitter.com/search?lang=en&q={keyword}%20lang%3A{lang}%20since%3A{since}%20{self.filter}&src=typed_query{self.type}'

        else:
            self.src= f'https://twitter.com/search?lang=en&q={keyword}%20lang%3A{lang}%20until%3A{until}%20{self.filter}&src=typed_query{self.type}'

    def scrape(self):
        try:
            if self.hide_bro:
                options = Options()
                options.add_argument("--headless")
                driver=Chrome(options=options)
            else:
                driver = Chrome()
            driver.get("https://www.twitter.com/i/flow/login")
            sleep(4)
            its_in=False
            while not its_in:
                try:
                    username = driver.find_element(By.XPATH, value='//input[@autocomplete="username"]')
                    username.send_keys(self.user_name)
                    username.send_keys(Keys.RETURN)
                    its_in = True
                    
                except:
                    driver.refresh()
                    sleep(7)
                    pass

                
            
            
            sleep(2)
            password = driver.find_element(By.XPATH, value='//input[@autocomplete="current-password"]')
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN) 
            print('Logged in successfully...')
            sleep(2)
            driver.get(self.src)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return 
        tweets = []
        tweet_ids=set()
        
        last_position = driver.execute_script("return window.pageYOffset;")
        scrolling = True
        
        while (len(tweets)<self.limit) and scrolling and self.error_count<20:
            try:
                cards=driver.find_elements(By.XPATH,value='//article[@data-testid="tweet" and @tabindex="0"]')
            except:
                print("Unexpected error:", sys.exc_info()[0])
                self.error_count += 1
                return tweets
            for card in cards:
                tweet = self._card_to_dic(card)
                if tweet:
                    tweet_id = tweet['tweet']
                    if tweet_id not in tweet_ids:
                        tweet_ids.add(tweet_id)
                        tweets.append(self._card_to_dic(card))
                        print(len(tweets))

            scroll_attempt = 0
            while True:
                driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
                sleep(3)
                cur_position = driver.execute_script("return window.pageYOffset;")
                if last_position == cur_position:
                    scroll_attempt += 1
                    if scroll_attempt >= 3:
                        scrolling = False
                        print('scrolling stopped')
                        break
                    else:
                        sleep(3)
                else:
                    last_position = cur_position
                    break
        return tweets
            
        
###################
    def _concat_text(self,card):
        output=''
        for i in card.find_elements(By.XPATH, value = './/span'):
            output+=i.text
        return output

    def _card_to_dic(self,card):
        dic={}
        try:
            time = card.find_element(By.XPATH,value='.//time').get_attribute('datetime')[:-5]
            dic['time'] = time
        except NoSuchElementException:
            return None
        try:
            id=card.find_element(By.XPATH,value='.//a[@tabindex="-1" and @role="link"]').get_attribute('href')[20:]
            dic['id'] = id
        except NoSuchElementException:
            return None
        
        try:
            tweet = self._concat_text(card.find_element(By.XPATH,value='.//div[@data-testid="tweetText"]'))
            dic['tweet'] = tweet
        except:
                print("Unexpected error:", sys.exc_info()[0])
                self.error_count += 1
                return None
        try:
            re = card.find_element(By.XPATH,value='.//div[@data-testid="reply"]').text
            dic['reply'] = int(''.join([i for i in re if i.isdigit()])) if len(re)>0 else 0
            ret = card.find_element(By.XPATH,value='.//div[@data-testid="retweet"]').text
            dic['retweet'] = int(int(''.join([i for i in ret if i.isdigit()]))) if len(ret)>0 else 0
            like = card.find_element(By.XPATH,value='.//div[@data-testid="like"]').text
            dic['like'] =  int(int(''.join([i for i in like if i.isdigit()]))) if len(like)>0 else 0
        except:
                print("Unexpected error:", sys.exc_info()[0])
                self.error_count += 1
                return None
        return dic
