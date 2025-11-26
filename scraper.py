#!/usr/bin/env python3
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from datetime import datetime


def fetch_example():
    url = "https://example.com"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    return {"url": url, "title": title, "fetched_at": datetime.utcnow().isoformat()}


def save_data(record, outdir="data"):
    os.makedirs(outdir, exist_ok=True)
    csv_path = os.path.join(outdir, "output.csv")
    df = pd.DataFrame([record])
    if os.path.exists(csv_path):
        df.to_csv(csv_path, mode="a", header=False, index=False)
    else:
        df.to_csv(csv_path, index=False)

    json_path = os.path.join(outdir, "output.json")
    with open(json_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Saved: {csv_path} and appended to {json_path}")


def main():
    try:
        rec = fetch_example()
        save_data(rec)
    except Exception as e:
        print("Error during scraping:", e)


if __name__ == "__main__":
    main()
