from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/job"
mongo = PyMongo(app)


def _to_dict(mongo_document) -> dict:
    return {
        'id': mongo_document['_id'],
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


@app.route('/offers/category/<string:category>')
def get_all_category_offers(category: str):
    offers = [_to_dict(offer) for offer in mongo.db.offers.find({'category': category})]
    return jsonify({'offers': offers})


@app.route('/offers/from/<string:city>')
def get_offers_from_city(city: str):
    offers = [_to_dict(offer) for offer in mongo.db.offers.find({'city': city})]
    return jsonify({'offers': offers})


if __name__ == '__main__':
    app.run(debug=True)
