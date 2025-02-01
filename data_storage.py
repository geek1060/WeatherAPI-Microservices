from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # Replace with your MySQL password
    database="weatherDB"
)

@app.route('/store_weather', methods=['POST'])
def store_weather():
    data = request.json
    cursor = db.cursor()
    query = "INSERT INTO weather_data (city, temperature, humidity) VALUES (%s, %s, %s)"
    values = (data['city'], data['temperature'], data['humidity'])
    cursor.execute(query, values)
    db.commit()
    return jsonify({"message": "Data stored successfully"}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
