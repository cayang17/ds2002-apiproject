from flask import Flask, jsonify, request
import pytz
from datetime import datetime
import json

app = Flask(__name__)

# Load the list of cities and their timezones from the cities.json file
with open('data/cities.json', 'r') as f:
    cities_db = json.load(f)

# Secret token for authorization
API_TOKEN = "your_secret_token_here"


# Function to check if the token is valid
def check_token(token):
    return token == API_TOKEN


@app.route("/get_time", methods=["GET"])
def get_time():
    # Retrieve the token from the headers
    token = request.headers.get("Authorization")

    # Check for valid token
    if not check_token(token):
        return jsonify({"error": "Unauthorized access. Invalid or missing token."}), 403

    # Get the city from the query parameter
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City parameter is required."}), 400

    # Check if the city is in the database
    if city not in cities_db:
        return jsonify({"error": f"City {city} is not in our database."}), 404

    # Get timezone based on the city
    timezone_str = cities_db[city]
    timezone = pytz.timezone(timezone_str)

    # Get the current time in the city's timezone
    local_time = datetime.now(timezone)
    utc_offset = local_time.strftime('%z')

    # Format the result into JSON
    response = {
        "city": city,
        "current_time": local_time.strftime('%Y-%m-%d %H:%M:%S'),
        "utc_offset": utc_offset
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
