from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_most_frequent_response


def create_bot(name):
    """ We have read_only to false so the chatbot
    learns from the user input

    Args:
        name (string): bot name
    Return:
        bot
    """
    bot = ChatBot(name = name,
                  logic_adapters = [
                                    {
                                    'import_path': 'chatterbot.logic.BestMatch',
                                    'default_response': "I don't understand.",
                                    'maximum_similarity_threshold': 0.90},
                                    #'chatterbot.logic.TimeLogicAdapter',
                                    'chatterbot.logic.MathematicalEvaluation',
                                    {
                                    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                                    'input_text': 'Help me!',
                                    'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
                                    }],
                  storage_adapter = "chatterbot.storage.SQLStorageAdapter",
                  database_uri='sqlite:///database.sqlite3',
                  response_selection_method=get_most_frequent_response,
                  read_only=False)
    
    return bot


def train_all_data(bot):
    """Train bot with a variety of topics
    We chose english but ca use other languages

    Args:
        Bot (chatterbot): chatterbot
    """
    corpus_trainer = ChatterBotCorpusTrainer(bot)
    corpus_trainer.train("chatterbot.corpus.english",
                        "chatterbot.corpus.english.greetings",
                        "chatterbot.corpus.english.conversations")
    
    
def custom_train(bot, conversation):
    """Train the bot with custom data, uses ListTrainer

    Args:
        bot ([chatterbot): chatterbot
        conversation (Array): array of two strings
    """
    trainer = ListTrainer(bot)
    trainer.train(conversation)
    
    
def predefined_train(bot):
    """Train the bot with data from training.txt
    
    Args:
        bot (chatterbot): chatterbot
    """
    training_data = []
    with open('training.txt', 'r') as f:
        for line in f:
            training_data.append(line.rstrip('\n'))
        
    print(training_data)
    i = 0
    while i < len(training_data) - 1:
        converstation = [training_data[i], training_data[i+1]]
        print(converstation)
        i += 2
        custom_train(bot, converstation)
    

def start_chatbot(bot):
    """Start and take responses from the catbot
    Chatbot stays running unless a word is typed from bye_list

    Args:
        bot (chatterbot): chatterbot
    """
    print("Hello, I am ChatterBot. How can I help you?")
    bye_list = ["bye bot", "bye", "good bye", "exit", "quit"] 
    
    while True:
        user_input = input("me: ")
        if user_input.lower() in bye_list:
            print("ChatterBot: Good bye, have a good day!")
            break
        
        response = bot.get_response(user_input)
        print("ChatterBot: ", response)
    