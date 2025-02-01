from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get_weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
