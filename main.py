import os
import logging
from flask import Flask, url_for, render_template, request

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def hello():
	logging.debug("Saying Hello")
	return render_template("home.html")

@app.route('/members')
def members():
	logging.debug("Displaying members")
	return render_template("members.html")		
