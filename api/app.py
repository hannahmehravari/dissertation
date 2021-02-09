import os
from flask import Flask, jsonify
from influxdb import InfluxDBClient
app = Flask(__name__)
db_client = InfluxDBClient(host='influxdb', port=8086)

#we define the route /
@app.route('/hi')
def welcome():
    # return a json
    return jsonify({'status': db_client.get_list_database()})

if __name__ == '__main__':
    #define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port 
    app.run(host='0.0.0.0', port=os.getenv('PORT'))