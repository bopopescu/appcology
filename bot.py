from __future__ import print_function
from flask import Flask, request, jsonify, g, Response
from helpers import send_response
from receive import Receiver
from send import Message
import json
import requests

'''
to deploy: 
git add .
git commit -m "message"
git push heroku master
'''
'''
to test before you deploy
source app/bin/activate (do only once in each terminal session)
python application.py
'''

GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

def response_handler(request):
	try:
		# Receive request
	    receiver = Receiver(request)

	    # User to send message back to
	    user_id = receiver.get_sender_messenger_id()

	    # Text from user
	    text = receiver.get_text()

	    response_text = check_for_greeting(text)

	    # Send message back
	    Message(response_text, user_id).send()
    	
	except e:
		print(e, file=sys.stderr)
		pass

	return send_response()


# Sentences we'll respond with if the user greeted us
def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    for word in sentence.words:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)
    return "I don't know what you said, fam."


