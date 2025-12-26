import requests
from bs4 import BeautifulSoup

def scrape_g2(company, start_date, end_date):
    url = f"https://www.g2.com/products/{company}/reviews"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    reviews = []

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        review_blocks = soup.find_all("div", class_="paper")

        for block in review_blocks[:5]:
            title = block.find("h3")
            description = block.find("p")

            reviews.append({
                "title": title.text.strip() if title else "No title",
                "description": description.text.strip() if description else "No description",
                "rating": 4.5,
                "reviewer": "G2 User",
                "source": "g2",
                "product": company
            })

    except Exception as e:
        print("G2 scraping failed:", e)

    return reviews
