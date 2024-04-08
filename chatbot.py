import re

# Define rules and responses
rules = {
    r'.*hello.*': 'Hi Buddy! I\'m chattur your chatbot.How can I assist you?',
    r'.*hiii.*': 'Hi there! How can I assist you?'
    r'.*how are you.*' 'I\'m just a bot, but thanks for asking!',
    r'.*weather.*': 'You can check the weather on weather.com.',
    r'.*bye.*': 'Goodbye! Have a great day!',
    r'.*help.*': 'Sure, I can help you. What do you need assistance with?',
    r'.*order.*pizza.*': 'I can\'t order pizza for you, but I can provide you with a list of local pizza restaurants.',
    r'.*tell me a joke.*': 'Bacon and eggs walk into a restaurant , the host says we dont serve breakfast here',
    r'.*fact.*': 'Did you know that a group of flamingos is called a "flamboyance"?',
    r'.*news.*': 'You can check the latest news on a news website like BBC or CNN.',
    r'.*movie.*recommendation.*': 'Sure! What genre are you interested in?'
}

# Function to match input with rules and provide response
def chatbot(input_text):
    for pattern, response in rules.items():
        if re.match(pattern, input_text.lower()):
            return response
    return "I'm sorry, can't help you with that ."

# Test the chatbot
while True:
    user_input = input("Your input : ")
    if user_input.lower() == 'exit':
        break
    print("Bot:", chatbot(user_input))

