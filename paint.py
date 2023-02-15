from flask import Flask, jsonify
import json
import random
app = Flask(__name__)

paintStyles = [
    {
        'maincolor': 'black',
        'altcolor': 'white',
        'style': 'checkered'
    },
    {
        'maincolor': 'black',
        'altcolor': 'yellow',
        'style': 'striped'
    },
    {
        'maincolor': 'purple',
        'altcolor': 'lime green',
        'style': 'spotted'
    }
]

@app.route('/')
def paint():
    
    randomNum = random.randint(0, len(paintStyles) - 1)
    return jsonify(paintStyles[randomNum])

app.run()
