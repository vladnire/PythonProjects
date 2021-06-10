import sys

from twitter_bot import TwitterBot


def menu():
    """Twitter bot menu"""
    
    bot = TwitterBot()
    
    user_input = ''
    menu_string = "\n1) Get Query\n"\
                  "2) Show Trends\n"\
                  "3) Show blocked users\n"\
                  "4) Show followers\n"\
                  "5) Get user tweets\n"\
                  "0) Exit\n"

    while user_input != 0:
        try:
            user_input = int(input(f"{menu_string}"))
        except ValueError:
            print("!!!Incorrect input, try again.!!!")
            next
            
        if user_input == 1:
            bot.get_query()
        elif user_input == 2:
            bot.show_trends()
        elif user_input == 3:
            bot.check_blocked_user()
        elif user_input == 4:
            bot.get_followers()
        elif user_input == 5:
            bot.get_user_tweets()
        elif user_input == 0:
            sys.exit('Bye!')


if __name__ == '__main__':
    menu()
