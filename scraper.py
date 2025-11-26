#!/usr/bin/env python3
"""Top-level entrypoint kept for backward compatibility.

Delegates to `dailyscraper.cli.main`.
"""
from dailyscraper.cli import main


if __name__ == "__main__":
    main()
