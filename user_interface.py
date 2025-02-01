from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    response = requests.get(f"http://192.168.56.101:5000/get_weather?city={city}").json()
    return render_template('result.html', data=response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
