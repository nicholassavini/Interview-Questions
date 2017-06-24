from flask import Flask
app = Flask(__name__)

import json
import random

@app.route('/')
def hello_world():
 return 'Hello World!'

@app.route('/dice', methods=['GET'])
def roll_dice():
    die_roll = int(random.randint(1,6))
    data = {'rolls':''}
    data['rolls'].append({
        'first_die' : die_roll
    })
    data['rolls'].append({
        'second_die' : die_roll
    })
    with open('data.txt', 'w') as file:
        json.dump(data, file)

if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0', port=8000)
