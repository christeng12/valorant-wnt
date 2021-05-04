import os
import logging
from flask import Flask, url_for, render_template, request
from riotwatcher import RiotWatcher, ValWatcher, ApiError

#  Static variables 
players = {"1":["WNT BigFella","WNT"]} # hardcoded, will retrieve dynamically from api later
region = "americas"
api_key = os.environ.get('API_KEY')
accWatcher = RiotWatcher(api_key)
valWatcher = ValWatcher(api_key)

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route('/home')
def hello():
	logging.debug("Saying Hello")
	return render_template("home.html")

@app.route('/members')
def members():
	logging.debug("Displaying members")
	content = accWatcher.account.by_riot_id(region,"WNT BigFella","WNT")
	logging.debug(content)
	return render_template("members.html")		
