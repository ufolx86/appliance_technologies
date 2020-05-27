from flask import Flask, jsonify
from flask_cors import CORS
from forex_python.bitcoin import BtcConverter
import numpy as np
import datetime
import json


# configuration
#DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/bitcoinPrices', methods=['GET'])
def returnDataSeries():
    #bitcoinPrices = np.zeros(4000,2)
    range_begin = datetime.datetime(2020, 1, 1, 19, 39, 36, 815417)
    range_end = datetime.datetime(2020, 5, 26, 19, 39, 36, 815417)
    b = BtcConverter()
    #get_previous_price(currency,date begin, date end)
    bitcoinPrices = b.get_previous_price_list('EUR', range_begin, range_end)
    return jsonify(bitcoinPrices)
    #return jsonify('pong!')
@app.route('/numpyArray', methods=['GET'])
def returnNumpyArray():
    npSeries = np.random.random((2,100))
    listSeries = npSeries.tolist()
    return jsonify(listSeries)
    # return "TEST_STRING"

if __name__ == '__main__':
    app.run(debug=True)

