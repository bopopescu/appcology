from flask import Flask, request, jsonify, g, Response, render_template
import bot
import os

# Elastic Beanstalk initalization
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello world! Nothing is broken!'


# Webhook route for Messenger

@application.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Here webhook is verified with Facebook Messenger.
        if request.args.get('hub.verify_token') == '12345':
            return Response(request.args.get('hub.challenge'))
        else:
            return Response('Wrong validation token')
    else:
        # Here messages are received, code for this is handled in bot.py.
        return bot.response_handler(request.get_json())



        


if __name__ == '__main__':
    application.debug = True
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0',port = port, debug = True)