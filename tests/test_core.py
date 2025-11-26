from dailyscraper.core import Scraper


def test_fetch_parses_title(monkeypatch):
    html = "<html><head><title>Test Page</title></head><body></body></html>"

    class FakeResponse:
        def __init__(self, text):
            self.text = text

        def raise_for_status(self):
            return None

    class FakeSession:
        def get(self, url, timeout=10):
            return FakeResponse(html)

    s = Scraper(session=FakeSession())
    rec = s.fetch("https://example.com")
    assert rec["title"] == "Test Page"
    assert rec["url"] == "https://example.com"
