from __future__ import print_function
from flask import Flask, request, jsonify, g, Response
from helpers import send_response
from receive import Receiver
from send import Message
import json
import requests
import random
import sys
from facepy import GraphAPI

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

SEPERATE TERMINAL WINDOWS
'''

GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's",)
GREETING_RESPONSE = "Hey! Welcome to Emory Events. Ask me what's going on around Emory."

ACCESS_TOKEN = 'EAAZAZC6jHx2vcBAEIwv2jUBIcXjlr2UgVvKHPJ9QgsWIhEggalW1K96YAuMXkKQMux9zjsWQfPUXWVsGK0ooWvGlwsZCoZAZClfpE6sv5Ntg9ECiJfruphS7gc9DQ1hy5DuGM9juzf7fb0eZCbUiHhhXrpJUELsNQucHOivKoLDgZDZD'
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
        	return GREETING_RESPONSE
        if 'event' in word:
        	return get_facebook_data()

def get_facebook_data():
	events = graph.get('me/events')

	data = []
	for event in events['data']:
		data.append(event['name'].encode('utf-8'))

	# firstEvent = events['data'][0]['name']
	dataString = str(data).strip('[]')

	return "Here are your Emory events: " + dataString
