import os
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)



@app.route('/door-test/', methods=('GET', 'POST'))
def create():
    return "This is the door"
