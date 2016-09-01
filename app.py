from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

textLogs ={}

@app.route('/', methods=['GET', 'POST'])
def index():
    """Respond to incoming calls with a simple text message."""
    resp = twilio.twiml.Response()
    resp.message("Lunch will be served at 1pm")
    return str(resp)

@app.route('/Contact')
def hello_world():
    return 'txt me!'
