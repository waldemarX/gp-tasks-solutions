import csv
from collections import Counter
from typing import Any

file_path = "file.csv"

AnyJSON = dict[str, Any]


def read_csv(file_path) -> list[AnyJSON]:
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter="|")
        data = [row for row in reader]
    return data


def collect_data(data) -> tuple[list[AnyJSON], list[AnyJSON]]:
    all_ids = [record["id"] for record in data]
    unique_ids = [id for id in all_ids if Counter(all_ids)[id] == 1]
    unique_records = []
    duplicate_records = []
    for record in data:
        if record["id"] in unique_ids:
            unique_records.append(record)
        else:
            duplicate_records.append(record)

    return unique_records, duplicate_records


def main():
    data = read_csv(file_path)
    unique_records, duplicate_records = collect_data(data)
    print(f"Unique records:\n {unique_records}")
    print(f"Duplicate records:\n {duplicate_records}")


if __name__ == "__main__":
    main()
