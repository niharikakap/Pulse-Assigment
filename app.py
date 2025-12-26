from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import json
import os

app = Flask(__name__)
CORS(app)  # Allow frontend requests

@app.route("/scrape", methods=["POST"])
def scrape_reviews():
    try:
        data = request.json
        company = data.get("company")
        source = data.get("source")
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        if not all([company, source, start_date, end_date]):
            return jsonify({"error": "Missing required fields"}), 400

        # Call scraper.py
        command = [
            "python", "scraper.py",
            "--company", company,
            "--source", source,
            "--start_date", start_date,
            "--end_date", end_date
        ]

        result = subprocess.run(command, capture_output=True, text=True)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

        if result.returncode != 0:
            return jsonify({"error": "Scraper failed", "details": result.stderr}), 500

        # Build output file path
        filename = f"{company}_{source}_reviews.json"
        filepath = os.path.join("output", filename)

        if not os.path.exists(filepath):
            return jsonify({"error": "reviews.json not created"}), 500

        with open(filepath, "r", encoding="utf-8") as f:
            reviews = json.load(f)

        return jsonify(reviews)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def home():
    return "Backend is running!"

if __name__ == "__main__":
    app.run(debug=True)
