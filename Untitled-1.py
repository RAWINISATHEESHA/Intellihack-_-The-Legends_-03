

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_most_frequent_response

chatbot = ChatBot(
    'SmartBankBot',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'statement_comparison_function': LevenshteinDistance,
            'response_selection_method': get_most_frequent_response
        }
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ]
)


trainer = ChatterBotCorpusTrainer(chatbot)


trainer.train('chatterbot.corpus.english')


print("Chatbot: Hi! I'm the Smart Bank chatbot. How can I assist you today?")
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("Chatbot:", response)


import os

if __name__ == "__main__":
    os.system("python chatbot.py")
