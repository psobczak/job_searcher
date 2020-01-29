from flask import Flask, jsonify, make_response
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/job"
mongo = PyMongo(app)


# db = DatabaseConnector()
# db.create_connection()
# d = Database('job', 'offers')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/offers', methods=['GET'])
def get_offers():
    offers = [offer for offer in mongo.db.offers.find()]
    return jsonify({'offers': offers})


@app.route('/offers/<int:offer_id>', methods=['GET'])
def get_offer(offer_id):
    return jsonify({'offer': db.get_all_offers()[offer_id]})


@app.route('/offers/<string:category>')
def get_all_category_offers(category):
    return jsonify({'offers': db.get_offers_with_category(category)})


@app.route('/offers/<string:category>/<int:offer_id>')
def get_category_offer(category, offer_id):
    return jsonify({'offers': db.get_offers_with_category(category)[offer_id]})


if __name__ == '__main__':
    app.run(debug=True)
