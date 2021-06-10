from flask import Flask, render_template, request
import sys

from chatbot_functions import *
        
        
def menu(bot):
    """Select run mode
    
    Args:
        bot (ChatterBot): chat bot
    """
    menu_string = "1) CLI Bot\n"\
                "2) Flask UI Bot\n"\
                "0) Exit\n"
                
    user_input = ''
    
    while user_input != 0:
        user_input = int(input(f"{menu_string}"))
        if user_input == 1:
            start_chatbot(bot)
        elif user_input == 2:
            run_flask(bot)
        elif user_input == 0:
            sys.exit('Bye!')
        else:
            sys.exit('Incorrect input, try again.')
    
        
def run_flask(bot):
    """Run ChatterBot in Flask

    Args:
        bot (ChatterBot): chat bot
    """
    app = Flask(__name__)
    
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/get")
    def get_bot_response():
        userText = request.args.get('msg')
        return str(bot.get_response(userText)) 
    
    app.run()
        
if __name__ == '__main__':

    # create chatbot 
    bot = create_bot('Chatterbot')

    # train all data
    train_all_data(bot)
    
    # train bot with wanted data from training.txt
    predefined_train(bot)
    
    # select run method
    menu(bot)