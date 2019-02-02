import os
import json
import re
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

app = Flask(__name__)
bot_id = "1520c98b3da635c8c6383951a6"
F_PATTERN = re.compile('can i get an? (.+) in the chat', flags=re.IGNORECASE | re.MULTILINE)
SUFFIX = '❤️'

@app.route("/", methods=["POST"])
def webhook():
    """
    Receive callback to URL when message is sent in the group.
    """
    # Retrieve data on that single GroupMe message.
    message = request.get_json()
    print("Message received: %s" % message)
    if message["sender_type"] != "bot":
        matches = F_PATTERN.search(message["text"]).groups()
        if len(matches):
            reply(matches[0] + ' ' + SUFFIX)

    return "ok", 200

def reply(text):
    """
    Reply in chat.
    """
    url = "https://api.groupme.com/v3/bots/post"
    data = {
        "bot_id": bot_id,
        "text": text,
    }
    request = Request(url, urlencode(data).encode())
    response = urlopen(request).read().decode()
    print("Response after message send: %s" % response)
