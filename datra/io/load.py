from pathlib import Path

import pandas as pd


_READERS = {
    ".csv": pd.read_csv,
    ".xlsx": pd.read_excel,
    ".xls": pd.read_excel,
}


def load(data):
    if isinstance(data, pd.DataFrame):
        return data.copy()

    if not isinstance(data, (str, Path)):
        raise TypeError(
            f"Unsupported input type: {type(data).__name__}."
        )

    path = Path(data)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    try:
        reader = _READERS[path.suffix.lower()]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported file type: '{path.suffix}'."
        ) from exc

    return reader(path)