def scrape_trustradius(company, start_date, end_date):
    return [
        {
            "title": f"TrustRadius review for {company}",
            "description": "Good overall experience.",
            "rating": 8.5,
            "reviewer": "TR User",
            "source": "trustradius",
            "product": company
        }
    ]
