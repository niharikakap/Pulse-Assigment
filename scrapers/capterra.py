import requests
from bs4 import BeautifulSoup

def scrape_capterra(company, start_date, end_date):
    url = f"https://www.capterra.com/p/{company}/reviews/"

    headers = {"User-Agent": "Mozilla/5.0"}
    reviews = []

    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        for block in soup.select("div.review")[:5]:
            title = block.find("h3")
            desc = block.find("p")

            reviews.append({
                "title": title.text.strip() if title else "No title",
                "description": desc.text.strip() if desc else "No description",
                "rating": 4.0,
                "reviewer": "Capterra User",
                "source": "capterra",
                "product": company
            })
    except Exception as e:
        print("Capterra scraping failed:", e)

    return reviews
