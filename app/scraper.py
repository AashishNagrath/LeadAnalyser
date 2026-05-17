import requests
from bs4 import BeautifulSoup


def scrape_website(url):

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No title found"

        meta_description = ""

        meta_tag = soup.find(
            "meta",
            attrs={"name": "description"}
        )

        if meta_tag:
            meta_description = meta_tag.get("content", "")

        headings = []

        for tag in soup.find_all(["h1", "h2", "h3"]):
            text = tag.get_text(strip=True)

            if text:
                headings.append(text)

        paragraphs = []

        for p in soup.find_all("p"):
            text = p.get_text(strip=True)

            if text:
                paragraphs.append(text)

        website_content = " ".join(paragraphs[:20])

        return {
            "title": title,
            "meta_description": meta_description,
            "headings": headings[:10],
            "content": website_content
        }

    except Exception as e:

        return {
            "error": str(e)
        }