from flask import Flask, jsonify, make_response

from config.database_connector import DatabaseConnector

app = Flask(__name__)

db = DatabaseConnector()
db.create_connection()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/offers', methods=['GET'])
def get_offers():
    return jsonify({'offers': db.get_all_offers()})


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
