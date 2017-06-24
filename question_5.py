from flask import Flask
from flask import Response

import json
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dice', methods=['GET'])
def roll_dice():
    ''' Generates a random dice roll and outputs JSON '''
    data = {'rolls': []}
    # "Roll the Dice" and add the results to the data dictionary
    for i in range(1, 3):
        data['rolls'].append({
            'roll_' + str(i): int(random.randint(1, 6))
        })
    # Send the proper response back to the browser so it knows that it's JSON
    response = Response(
        response=json.dumps(data, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
