#!/usr/bin/env python3

"""
Script for building the static website.
"""

# Import Python standard libraries
import logging
from pathlib import Path

# Import our library
import static_html

# TODO: temporary method only for setting up Netlify
def build_html(site_path):
    index_path = site_path / "index.html"

    with open(index_path.as_posix(), "w") as handler:
        handler.write("Thot is here")


def main():
    """
    Entry point for the script.
    """

    # Obtain `base_path` for file manipulation
    base_path = Path(__file__).parent.resolve()

    # Load JSON configuration and replaces, and include paths in the first
    config, replaces = static_html.load_config(base_path)
    config["base_path"] = base_path
    config["output_path"] = base_path / config["output_path"]

    # Read raw data
    raw_data = static_html.read_data(config)

    # Build site
    static_html.render_html(raw_data, replaces, config)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
