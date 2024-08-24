from flask import Flask, request, jsonify
from geo_aip import GeoAIP

app = Flask(__name__)
api = GeoAIP()

@app.route('/data/ingest', methods=['POST'])
def ingest_data():
    filepath = request.json.get('filepath')
    data = api.ingest_data(filepath)
    return jsonify({"status": "success", "data": data})

@app.route('/data/query', methods=['GET'])
def query_data():
    lat = float(request.args.get('lat'))
    long = float(request.args.get('long'))
    result = api.query_data(lat, long)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
