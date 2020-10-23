import common as c
import re

patterns = {}

# Iterate over the keywords dictionary
for intent, keys in c.keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile('|'.join(keys))

# Define a function to find the intent of a message
def match_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message 
        match = re.search(pattern, message)
        if match is not None:
            matched_intent = intent
    return matched_intent

# Define a respond function
def respond(message):
    # Call the match_intent function
    intent = match_intent(message)
    # Fall back to the default response
    key = "default"
    if intent in c.responses:
        key = intent
    return c.responses[key]

def send_message(message):
    print(c.user_template.format(message))
    print(c.bot_template.format(respond(message)))
    print('')

# Send messages
send_message("hello!")
send_message("which every one") #matches for "hi" in a word
send_message("bye byeee")
send_message("thanks very much!")