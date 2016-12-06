from flask import Flask, request, jsonify, g, Response
from datetime import datetime, timedelta
from pytz import timezone
import json

def send_response():
    response = jsonify({})
    response.status_code = 200
    return response

