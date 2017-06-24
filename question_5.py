from flask import Flask
from flask import Response
app = Flask(__name__)

import json
import random

@app.route('/')
def hello_world():
 return 'Hello World!'

@app.route('/dice', methods=['GET'])
def roll_dice():
    data = {'rolls':[]}
    for i in range(1, 3):
        data['rolls'].append({
            'roll_' + str(i) : int(random.randint(1,6))
        })
    response = Response(
        response=json.dumps(data, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0', port=8000)

