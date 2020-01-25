from flask import Flask, request, jsonify
from random import random
import pymongo

# remember to install dnspython, special pymongo install, flask, pyOpenSSL 
# uwsgi
app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://username:123@cluster0-wd3pf.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

# params: url:
@app.route('/detect/url', methods = ['POST'])
def detect_url():
    pass

# params: text:
@app.route('/detect/text', methods = ['POST'])
def detect_text():
    text = request.json['text']
    print(text)
    response = {"prediction": random()}
    return jsonify(response)



@app.route('/')
def test():
    return jsonify({"test":"food"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True) #ssl_context='adhoc')

# @ classify text
# expects raw text, returns prediction

# @ classify url
# expects url, returns prediction and url info

