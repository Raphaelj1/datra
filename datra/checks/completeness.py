import pandas as pd


def completeness(df: pd.DataFrame):
    total_rows = len(df)

    result = {}

    for col in df.columns:
        missing = df[col].isna().sum()
        filled = total_rows - missing

        result[col] = {
            "missing_values": int(missing),
            "filled_values": int(filled),
            "completeness_ratio": float(round(filled / total_rows, 4))
        }

    return result