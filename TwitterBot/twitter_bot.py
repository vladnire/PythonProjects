import tweepy
import sys
from tweepy import OAuthHandler

import config

class TwitterBot:
    
    def __init__(self):
        auth = OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
        auth.set_access_token(config.ACESS_TOKEN, config.ACCESS_SECRET)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        
        # Verify authentication
        try:
            self.api.verify_credentials()
        except Exception as e:
            raise e("!!!Error during authentication!!!")
        print("-----Authentication Ok. API connected.-----")
        
    def get_query(self):
        """Prints 5 tweets based on user query"""
    
        print("-----Tweets Query----")
        query = str(input("Please input twitter query: "))
        try:
            # Creation of query method using parameters
            tweets = tweepy.Cursor(self.api.search, q=query).items(5)
            for tweet in tweets:
                user = tweet.user.name
                text = tweet.text.replace('\n\n','\n')
                print(f"[{user}]: {text} \n")
        except BaseException as e:
            print(f'Failed on status {e} {str(e)}')
                
    def show_trends(self):
        """Show top 10 trends https://nations24.com/"""
        
        menu_string = "\n1) UK Trends\n"\
                "2) US Trends\n"
                
        user_input = int(input(f"{menu_string}"))
        
        if user_input == 1:
            trends_result = self.api.trends_place(23424975)
        elif user_input == 2:
            trends_result = self.api.trends_place(23424977)
        else:
            sys.exit('Incorrect input')
        
        print("-----Trends-----")
        for trend in trends_result[0]["trends"][:10]:
            print(trend["name"])

    def check_blocked_user(self):
        """Print blocked users"""
        print("-----Blocked Accounts-----")
        for block in self.api.blocks():
            print(block.name)
            
    def get_followers(self):
        """Print followers"""
        print("-----Followers-----")
        for follower in self.api.followers():
            print(follower.screen_name)
    
    def get_user_tweets(self):
        """Get User Last 5 Tweets"""
        print("-----Get User Tweets-----")
        user_id = str(input("Please input user id: "))
        
        user_tweets = self.api.user_timeline(screen_name=user_id, 
                           # 200 is the maximum allowed count
                           count=5,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
        
        for tweet in user_tweets:
            #print("ID: {}".format(tweet.id))
            print(tweet.created_at)
            print(tweet.full_text)
            #print("\n")
