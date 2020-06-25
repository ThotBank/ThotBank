#!/usr/bin/env python3

"""
Script for building the static website.
"""

# Import Python standard libraries
import logging
from pathlib import Path

# TODO: temporary method only for setting up Netlify
def build_html(site_path):
    index_path = site_path / "index.html"

    with open(index_path.as_posix(), "w") as handler:
        handler.write("Thot is here")


def main():
    """
    Entry point for the script.
    """

    # Build path for the HTML output directory
    site_path = Path(__file__).parent / "_site"

    # Build site
    build_html(site_path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
