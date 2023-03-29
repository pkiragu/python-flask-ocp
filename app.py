from time import sleep
from flask import Flask
from redis import Redis, RedisError
import os
import socket
import requests
import json
import time
import urllib3
urllib3.disable_warnings()
import sys
import instana


app = Flask(__name__)

@app.route("/")
def hello():

    url = os.getenv('URL')
    headers = {"content-type": "application/json; charset=utf-8" }

    data = {
        "VoterName": "Peter G",
        "VoterAddress":"Test Address",
        "VotingIntention": "B"
        }

    print("Sending request to " + url)
    response = requests.post(url, headers=headers, json=data)
    print("Status Code", response.status_code)
    print("Response: ", response.text)
    #time.sleep(5)

    html = "<h3>Hello {name}!</h3>" \
            "<b>Sent request to: {url}<br/>"
    return html.format(name=os.getenv("NAME", "APIC User"), url=os.getenv("URL","https://default.svc"))
    return 'My hostname is %s'

    
    #print("JSON Response ", response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
