#!/usr/bin/env python3

"""
Module for generating SQL data from raw_data.
"""

# Import Python standard libraries
import csv
from pathlib import Path
import sqlite3


def read_tsv_data(filepath):
    with open(filepath.as_posix()) as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter="\t")
        data = list(reader)

    return data


def main():
    # Build database and raw data paths
    raw_data = Path(__file__).parent / "raw_data"
    db_path = Path(__file__).parent / "db" / "thotbank.db"

    # Delete any previous version of the database, create a new handler
    # and add tables
    if db_path.exists():
        db_path.unlink()
    conn = sqlite3.connect(db_path.as_posix())
    conn.execute("""CREATE TABLE roots (id integer, formegyroot text)""")

    # Read root table as lists of dictionaries and add them
    roots = read_tsv_data(raw_data / "roots.tsv")
    for entry in roots:
        command = (
            f"""INSERT INTO roots VALUES ({entry['ID']}, '{entry['FormEgyRoot']}')"""
        )
        conn.execute(command)

    # Close database handler
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
