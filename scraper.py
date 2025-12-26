import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from scrapers.g2 import scrape_g2
from scrapers.capterra import scrape_capterra
from scrapers.trustradius import scrape_trustradius
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# -----------------------------
# Normalize rating
# -----------------------------
def normalize_rating(rating, source):
    try:
        rating = float(rating)
        if source == "trustradius":
            return round((rating / 10) * 5, 1)
        return round(rating, 1)
    except:
        return None

# -----------------------------
# API Route
# -----------------------------
@app.route("/scrape", methods=["POST"])
def scrape_reviews():
    data = request.json

    company = data.get("company")
    source = data.get("source")
    start_date = data.get("start_date")  # Optional
    end_date = data.get("end_date")      # Optional

    if not company or not source:
        return jsonify({"error": "Missing company or source"}), 400

    # Call the appropriate scraper
    try:
        if source == "g2":
            reviews = scrape_g2(company, start_date, end_date)
        elif source == "capterra":
            reviews = scrape_capterra(company, start_date, end_date)
        elif source == "trustradius":
            reviews = scrape_trustradius(company, start_date, end_date)
        else:
            return jsonify({"error": "Invalid source"}), 400

        # Normalize ratings for all reviews
        for review in reviews:
            review["rating"] = normalize_rating(review.get("rating"), source)
            review["source"] = source
            review["product"] = company

        return jsonify(reviews)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Backend running on http://127.0.0.1:5000")
    app.run(debug=False, use_reloader=False)
