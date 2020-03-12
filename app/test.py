from flask import Flask, request, jsonify
from random import random


# remember to install dnspython, special pymongo install, flask, pyOpenSSL 
# uwsgi
app = Flask(__name__)

@app.route('/')
def test():
    return jsonify({"test":"food"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True) #ssl_context='adhoc')

# @ classify text
# expects raw text, returns prediction

# @ classify url
# expects url, returns prediction and url info

