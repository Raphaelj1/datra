import re
import pandas as pd


def standardize_column_names(df: pd.DataFrame):
    cleaned = df.copy()

    cleaned.columns = [
        _standardize(column)
        for column in cleaned.columns
    ]

    return cleaned


def _standardize(name: str) -> str:
    name = name.strip()

    #Ssplit acronym followed by a normal word.
    # HTTPStatus -> HTTP_Status
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)

    # Split lowercase/ditgit followed by uppercase
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)

    # Replace any non-alphanumeric characters with underscores
    name = re.sub(r"[^A-Za-z0-9]+", "_", name)

    # Collapse repeated underscores
    name = re.sub(r"_+", "_", name)

    # Remove leading/trailing underscores.
    name = name.strip("_")

    return name.lower()