"""Command-line interface for the scraper."""
import argparse
from .core import Scraper
from .io import save_record


def make_parser():
    p = argparse.ArgumentParser(prog="scraper", description="Daily Data Scraper CLI")
    p.add_argument("--url", default="https://example.com", help="Target URL to scrape")
    p.add_argument("--outdir", default="data", help="Directory to save outputs")
    p.add_argument("--dry-run", action="store_true", help="Don't write files; just show targets")
    return p


def main(argv=None):
    parser = make_parser()
    args = parser.parse_args(argv)

    s = Scraper()
    rec = s.fetch(args.url)
    csv_path, json_path = save_record(rec, outdir=args.outdir, dry_run=args.dry_run)

    if args.dry_run:
        print(f"Dry run — would write: {csv_path} and {json_path}")
    else:
        print(f"Saved: {csv_path} and appended to {json_path}")


if __name__ == "__main__":
    main()
