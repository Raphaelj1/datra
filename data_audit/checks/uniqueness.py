import pandas as pd


def uniqueness(df: pd.DataFrame):
    total_rows = len(df)

    dup_mask = df.duplicated()
    duplicate_rows = dup_mask.sum()

    result = {
        "total_rows": total_rows,
        "duplicate_rows": int(duplicate_rows),
        "duplicate_ratio": float(round(duplicate_rows / total_rows, 4) if total_rows else 0),
        "duplicate_sample": df[dup_mask].head(5).to_dict(orient="records")
    }

    return result