"""
Module for data validation.
"""

# TODO: integrate with tests later

from pathlib import Path


def main():
    """
    Main function for data validation, intended for user execution.
    """

    # Build path to raw data
    raw_data = Path(__file__).parent / "raw_data"

    # TODO: currently only validating if all files exist
    roots_file = raw_data / "roots.tsv"
    if not roots_file.exists():
        raise AssertionError("`roots.tsv` is missing.")

    tla_file = raw_data / "tla.tsv"
    if not tla_file.exists():
        raise AssertionError("`tla.tsv` is missing.")

    ccl_file = raw_data / "ccl.tsv"
    if not ccl_file.exists():
        raise AssertionError("`ccl.tsv` is missing.")

    vycichi_file = raw_data / "vycichi.tsv"
    if not vycichi_file.exists():
        raise AssertionError("`vycichi.tsv` is missing.")

    osing_file = raw_data / "osing.tsv"
    if not osing_file.exists():
        raise AssertionError("`osing.tsv` is missing.")


if __name__ == "__main__":
    main()
