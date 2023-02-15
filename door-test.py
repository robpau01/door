import os
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)



@app.route('/door-test/')
def index():
    return "This is the door"
