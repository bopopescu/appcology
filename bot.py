from flask import Flask, request, jsonify, g, Response
from helpers import send_response
from receive import Receiver
from send import Message
import json
import requests


GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

def response_handler(request):
	try:
		# Receive request
	    receiver = Receiver(request)

	    # User to send message back to
	    user_id = receiver.get_sender_messenger_id()

	    # Text from user
	    text = receiver.get_text(hi)

	    # Send message back
	    Message(text, user_id).send(hi)
    	
	except:
		pass

	return send_response()


# Sentences we'll respond with if the user greeted us


