from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/proxy', methods=['GET'])
def proxy():
    try:
        # Extract query parameters from the request
        lat = request.args.get('lat')
        lon = request.args.get('lon')
        stdate = request.args.get('start')
        eddate = request.args.get('end')
        api_key = '1f729eb41eeba325f71a7228682af68a'

        # Construct the API URL
        api_url = f'http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={stdate}&end={eddate}&appid={api_key}'

        # Make the actual request to the external API
        response = requests.get(api_url)
        data = response.json()

        # Send the API response back to the client
        return jsonify(data), 200
    except Exception as e:
        print(f'Error fetching data: {e}')
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
