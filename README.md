# Pulse-Assignment: Product Reviews Scraper

A *Product Reviews Scraper* that collects reviews from **G2**, **Capterra**, and **TrustRadius** (bonus source) for a specified company and time period. The scraped reviews are saved in a structured JSON format for easy analysis.

---

## Features

- Scrape reviews from **G2**, **Capterra**, and **TrustRadius**.
- Accepts the following inputs:
  - **Company Name**
  - **Start Date**
  - **End Date**
  - **Source** (`g2`, `capterra`, `trustradius`)
- Normalizes ratings to a **1–5 scale** for consistency.
- Outputs JSON files with:
  - `title`: Review title
  - `description`: Full review content
  - `date`: Review posting date
  - `reviewer`: Reviewer name
  - `rating`: Review rating (1–5)
  - `source`: Review platform
  - `product`: Product name
- Easily extendable to add additional review sources.
- Handles errors and invalid inputs gracefully.
- Bonus: **TrustRadius integration** for SaaS app reviews.

---

## Project Structure


review_scraper/
├─ scrapers/
│  ├─ **init**.py
│  ├─ g2.py
│  ├─ capterra.py
│  └─ trustradius.py
├─ output/
├─ scrape_reviews.py
├─ requirements.txt
└─ README.md

- `scrapers/` – Contains modules for each review source.  
- `output/` – JSON files are saved here.  
- `scrape_reviews.py` – Main script to run the scraper.  
- `requirements.txt` – Python dependencies.  


## Installation

1. Clone the repository:

bash
git clone https://github.com/niharikakap/Pulse-Assigment.git
cd Pulse-Assigment


2. (Optional) Create a virtual environment:

bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate


3. Install dependencies:

bash
pip install -r requirements.txt



##Usage

Run the scraper script:

bash
python scrape_reviews.py


You will be prompted to enter:

* Company Name (e.g., `Hubspot`)
* Start Date (YYYY-MM-DD, e.g., `2023-01-01`)
* End Date(YYYY-MM-DD, e.g., `2023-12-31`)
* **Source** (`g2`, `capterra`, or `trustradius`)

The scraped reviews will be saved in:


output/reviews.json



## Sample JSON Output
json
[
    {
        "title": "Great experience with Hubspot",
        "description": "I really liked using Hubspot. Very helpful product.",
        "date": "2023-06-10",
        "reviewer": "Verified User",
        "rating": 4.5,
        "source": "g2",
        "product": "Hubspot"
    },
    {
        "title": "Good value for money",
        "description": "Hubspot is reliable and easy to use.",
        "date": "2023-09-15",
        "reviewer": "Business User",
        "rating": 4.0,
        "source": "capterra",
        "product": "Hubspot"
    }
]




## Notes & Limitations

* Current scrapers use *placeholder data*. Real scraping may require:

  * Official APIs (if available)
  * Selenium or Playwright for dynamic web pages
* Pagination handling can be implemented inside scraper modules.
* Ensure correct **date formats (`YYYY-MM-DD`)** when entering start and end dates.

---

## Bonus: TrustRadius Integration

* TrustRadius ratings are normalized from **0–10** to **1–5 scale** for consistency.
* Use `trustradius` as the source input when prompted.
* Works with the same structure and output as G2 and Capterra.

---

## License

This project is licensed under the **MIT License**.
