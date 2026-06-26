from pathlib import Path

import pandas as pd


def _save_csv(df: pd.DataFrame, path: Path):
    df.to_csv(path, index=False)


def _save_excel(df: pd.DataFrame, path: Path):
    df.to_excel(path, index=False)


_WRITERS = {
    ".csv": _save_csv,
    ".xlsx": _save_excel,
    ".xls": _save_excel,
}

def _resolve_suffix(output: Path, format):
    if format is not None:
        suffix = "." + format.lower().lstrip(".")
        output = output.with_suffix(suffix)
    else:
        suffix = output.suffix.lower()

    return output, suffix

def save(df: pd.DataFrame, output, format=None):
    output = Path(output)

    output, suffix = _resolve_suffix(output, format)
    
    if suffix not in _WRITERS:
        supported = ", ".join(_WRITERS.keys())
        raise ValueError(
            f"Unsupported file format '{suffix}'. Supported formats are: {supported}"
        )
    
    writer = _WRITERS[suffix]

    output.parent.mkdir(parents=True, exist_ok=True)

    writer(df, output)

    return output