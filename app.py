import json
from flask import Flask, jsonify
from pymongo import MongoClient
from bson import json_util
import urllib

app = Flask(__name__)


def get_database():
    CONNECTION_STRING = "mongodb+srv://sam:" + \
        urllib.parse.quote(
            "12340987") + "@cluster0.cfkt66x.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db = client['product_list']
    col = db["products"]
    # temp = [{"productId": "12445dsd234", "category": "Modile", "productName": "Samsung",
    #          "productModel": "GalaxyNote", "price": 700, "availableQuantity": 10
    #          }, {
    #     "productId": "123245ds4234", "category": "TV",
    #     "productName": "Sony", "productModel": "Bravia", "price": 1200, "availableQuantity": 6}
    # ]
    # col.insert_many(temp)
    return col


def parse_data(data):
    return json.loads(json_util.dumps(data))


@app.route('/rest/v1/products', methods=['GET'])
def products():
    try:
        mongo_col = get_database()
        data = mongo_col.find()
        product_list = parse_data(data)
        return jsonify({"products": product_list})

    except Exception as e:
        print(e)
        return jsonify({"error": e})


if __name__ == '__main__':
    app.run()
    # get_database()
