from flask import Flask, request, jsonify, g, Response
from helpers import send_response
from receive import Receiver
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
	    m = Message(text, user_id)
    	m.send()

    	return send_response()

	except:
		return send_response()