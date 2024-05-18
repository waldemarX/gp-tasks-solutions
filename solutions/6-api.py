from datetime import datetime
from typing import Any
from pydantic import BaseModel
from pandas import DataFrame
import httpx


class Document(BaseModel):
    Columns: list[str]
    Description: str
    RowCount: int
    Rows: list[list[Any]]


today = datetime.now()
url = f"https://api.gazprombank.ru/very/important/docs?documents_date={today.date()}"


def json_to_dataframe(data) -> DataFrame:
    columns = data["Columns"]
    rows = data["Rows"]
    df = DataFrame(rows, columns=columns)

    column_mapping = {
        "key1": "document_id",
        "key2": "document_dt",
        "key3": "document_name",
    }

    df.rename(columns=column_mapping, inplace=True)

    df["load_dt"] = today

    return df


def main():
    data = httpx.get(url).json()
    validated_data = Document(**data)
    json_to_dataframe(validated_data.model_dump())


if __name__ == "__main__":
    main()
