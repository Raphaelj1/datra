import pandas as pd


def profile(df: pd.DataFrame):
    rows, columns = df.shape

    numeric_columns = len(
        df.select_dtypes(include="number").columns
    )

    categorical_columns = len(
        df.select_dtypes(include=["object", "category"]).columns
    )

    datetime_columns = len(
        df.select_dtypes(include=["datetime64"]).columns
    )

    memory_usage_mb = float(round(
        df.memory_usage(deep=True).sum() / (1024 * 1024),
        2
    ))

    duplicate_rows = int(df.duplicated().sum())

    missing_cells = int(df.isna().sum().sum())
    
    # columns = {}

    # for col in df.columns:
    #     col_data = df[col]

    #     columns[col] = {
    #         "dtype": str(col_data.dtype),
    #         "missing_pct": round(col_data.isna().mean() * 100, 2),
    #         "unique_count": int(col_data.nunique(dropna=True)),
    #         "sample_values": col_data.dropna().astype(str).head(3).tolist()
    #     }

    return {
        "rows": rows,
        "columns": columns,
        "numeric_columns": numeric_columns,
        "categorical_columns": categorical_columns,
        "datetime_columns": datetime_columns,
        "memory_usage_mb": memory_usage_mb,
        "duplicate_rows": duplicate_rows,
        "missing_cells": missing_cells,
    }