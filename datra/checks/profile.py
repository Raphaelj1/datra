import pandas as pd


def profile(df: pd.DataFrame):
    summary = {}

    summary["shape"] = {
        "rows": df.shape[0],
        "columns": df.shape[1]
    }

    summary["memory_usage_kb"] = round(df.memory_usage(deep=True).sum() / 1024, 2)

    columns = {}

    for col in df.columns:
        col_data = df[col]

        columns[col] = {
            "dtype": str(col_data.dtype),
            "missing_pct": round(col_data.isna().mean() * 100, 2),
            "unique_count": int(col_data.nunique(dropna=True)),
            "sample_values": col_data.dropna().astype(str).head(3).tolist()
        }

    summary["columns"] = columns

    return summary