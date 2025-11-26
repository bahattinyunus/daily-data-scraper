"""I/O helpers for saving scraped records."""
import os
import json
import pandas as pd


def save_record(record: dict, outdir: str = "data", dry_run: bool = False):
    """Save record to CSV and append a JSON line. Creates `outdir` if needed.

    If `dry_run` is True, nothing is written and a tuple of target paths is returned.
    """
    os.makedirs(outdir, exist_ok=True)
    csv_path = os.path.join(outdir, "output.csv")
    json_path = os.path.join(outdir, "output.json")

    if dry_run:
        return csv_path, json_path

    df = pd.DataFrame([record])
    if os.path.exists(csv_path):
        df.to_csv(csv_path, mode="a", header=False, index=False)
    else:
        df.to_csv(csv_path, index=False)

    with open(json_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    return csv_path, json_path
