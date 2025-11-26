"""Core scraping logic.

Provides a testable Scraper class that fetches a URL and extracts a simple
record (title + metadata). Designed to be small and easy to extend.
"""
from datetime import datetime
import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, session=None):
        self.session = session or requests.Session()

    def fetch(self, url: str, timeout: int = 10) -> dict:
        """Fetch the `url` and return a record containing title and timestamp."""
        resp = self.session.get(url, timeout=timeout)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        title = soup.title.string.strip() if soup.title and soup.title.string else ""
        return {"url": url, "title": title, "fetched_at": datetime.utcnow().isoformat()}
