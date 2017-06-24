from flask import Flask
app = Flask(__name__)

import json
import random

@app.route('/')
def hello_world():
 return 'Hello World!'

if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0', port=8000)
