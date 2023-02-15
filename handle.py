app = Flask(__name__)


@app.route('/handle')
def get_handle():
    data = {
        'color': 'Yellow',
        'material': 'Wood',
        'shape': 'Round',
    }
    response = app.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )
    return response


app.run()"
