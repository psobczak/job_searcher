import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_all_offers(offers=None):
    offers = requests.get('http://localhost:5000/offers').json()['offers']
    return render_template('hello.html', offers=offers)


if __name__ == '__main__':
    app.run(debug=True, port=80)
