from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://db:27017/job"
mongo = PyMongo(app)


def _to_dict(mongo_document):
    return {
        'title': mongo_document['title'],
        'source': mongo_document['source'],
        'link': mongo_document['link'],
        'minimal_salary': mongo_document['minimal_salary'],
        'maximal_salary': mongo_document['maximal_salary'],
        'employer': mongo_document['employer'],
        'address': mongo_document['address'],
        'city': mongo_document['city'],
        'category': mongo_document['category'],
        'posted': mongo_document['posted']
    }


@app.route('/offers', methods=['GET'])
def get_offers():
    offers = [_to_dict(offer) for offer in mongo.db.offers.find()]
    return jsonify({'offers': offers})


@app.route('/offers/category/<string:category>', methods=['GET'])
def get_all_category_offers(category):
    offers = [_to_dict(offer) for offer in mongo.db.offers.find({'category': category})]
    return jsonify({'offers': offers})


@app.route('/offers/city/<string:city>', methods=['GET'])
def get_offers_from_city(city):
    offers = [_to_dict(offer) for offer in mongo.db.offers.find({'city': city})]
    return jsonify({'offers': offers})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
