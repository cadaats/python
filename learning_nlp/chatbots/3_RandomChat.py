# Import the random module
import random

bot_template = "BOT : {0}"
user_template = "USER : {0}"

name = "Greg"
weather = "cloudy"

# Define a dictionary containing a list of responses for each message
responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "default": ["default message"]
}

# Use random.choice() to choose a matching response
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return a random matching response
        bot_message = random.choice(responses[message])
    else:
        # Return a random "default" response
        bot_message = random.choice(responses["default"])
    return bot_message

def send_message(message):
    print(user_template.format(message))
    print(bot_template.format(respond(message)))
    print('')

# Test function
send_message("what's today's weather?")
send_message("what's your name?")
send_message("who are you?")