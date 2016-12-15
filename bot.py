from __future__ import print_function
from flask import Flask, request, jsonify, g, Response
from helpers import send_response
from receive import Receiver
from send import Message, ACCESS_TOKEN
import json
import requests
import random
import sys
from facepy import GraphAPI
# import facebook

'''
to deploy: 
git add .
git commit -m "message"
git push heroku master


how to push to github
git add .
git commit -m "message"
git push origin master

'''
'''
to test before you deploy
source app/bin/activate (do only once in each terminal session)
python application.py
'''
'''
SEPERATE TERMINAL WINDOWS
'''

GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's",)
GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

# graph = facebook.GraphAPI(access_token=ACCESS_TOKEN, version='2.2')
graph = GraphAPI(ACCESS_TOKEN)

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
    	
	except Exception as inst:
		print(inst, file=sys.stderr)
		pass

	return send_response()


# Sentences we'll respond with if the user greeted us
def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    words = sentence.split()
    for word in words:
    	if word in GREETING_KEYWORDS:
        	return GREETING_RESPONSES[random.randint(0, len(GREETING_RESPONSES)-1)]
    return get_facebook_data() # change to get_facebook_data() and have it return a word (String)


def get_facebook_data():

	events = graph.get('me/events')
	data = []
	for event in events['data']:
    	data.append(event['name'])

	return "Here are Emory's events: " + data
