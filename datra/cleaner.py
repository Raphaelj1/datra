import pandas as pd


def clean(df: pd.DataFrame, rules: dict):
    cleaned_df = df.copy()

    report = {
        "duplicates_removed": 0,
        "missing_values_filled": 0,
        "rows_dropped": 0,
    }

    return cleaned_df, report