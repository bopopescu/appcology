from flask import Flask, request, jsonify, g, Response
from helpers import send_response
from receive import Receiver
from send import Message
import json
import requests


def response_handler(request):
	try:
		# Receive request
	    receiver = Receiver(request)

	    # User to send message back to
	    user_id = receiver.get_sender_messenger_id()

	    # Text from user
	    text = receiver.get_text()

	    # Send message back
	    Message(text, user_id).send()
    	
	except:
		pass

	return send_response()