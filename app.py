from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message("Listening to BadBadNotGood's Drowning!")
    return str(resp)

@app.route('/Contact')
def hello_world():
    return 'txt me!'
