import csv


def tsv_as_dict(filepath):
    table_data = {"columns": None, "rows": []}

    with open(filepath) as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter="\t")
        for row in reader:
            # Get columns if missing
            # TODO: determine somewhere else, also type
            if not table_data["columns"]:
                table_data["columns"] = [
                    {"datatype": "string", "name": column}
                    for column in list(row.keys())
                ]

            table_data["rows"].append(
                [
                    {"url": None, "value": row[col["name"]]}
                    for col in table_data["columns"]
                ]
            )

    return table_data


def read_data(config):
    raw_data = {}
    for table in config["tables"]:
        # Build file path
        table_path = "%s.tsv" % table
        table_path = config["base_path"] / "raw_data" / table_path

        # Read and store data
        raw_data[table] = tsv_as_dict(table_path.as_posix())

    return raw_data
