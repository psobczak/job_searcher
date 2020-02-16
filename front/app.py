import requests
from flask import Flask, render_template

app = Flask(__name__)


def sort_offer_by_key(offers, key):
    return sorted(offers, key=lambda offer: offer[key])


@app.route('/', methods=['GET'])
def get_all_offers(offers=None):
    offers = requests.get('http://localhost:5000/offers').json()['offers']
    return render_template('content.html', offers=sort_offer_by_key(offers, 'source'))


@app.route('/city/<string:city>')
def get_offers_from_city(city):
    offers = requests.get(f'http://localhost:5000/offers/from/{city}').json()['offers']
    return render_template('content.html', offers=sort_offer_by_key(offers, 'source'))


if __name__ == '__main__':
    app.run(debug=True, port=80)
