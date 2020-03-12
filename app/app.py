from request import make_request
from flask import Flask, request, jsonify
from random import random
import pymongo
from datetime import datetime 
# remember to install dnspython, special pymongo install, flask, pyOpenSSL 
# uwsgi
app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://username:123@cluster0-wd3pf.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

# params: url:
@app.route('/detect/url', methods = ['POST'])
def detect_url():
    url = request.json['url']
    title, author, txt = make_request(url)
    predictions = [x1,x2,x3,x4,x5,x6]
    [x1, x2, x3, x4, x5, x6] = [1, 2, 3, 4, 5, 6]
    cred = (100 / 12) * (1 * x1 + 3 * x2 + 5 * x3 + 7 * x4 + 9 * x5 + 11 * x6)
    category = "pants-on-fire"
    response = {"title": title, "author": author, "cred": cred, "category": category}
    return jsonify(response)

def save_time()
    date, time = datetime.now().strftime('%D %H:%M:%S').split(' ')
    db = client.test
# not done handling the databse

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

