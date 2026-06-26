import pandas as pd


def fill_missing(df: pd.DataFrame, rules: dict):
    cleaned = df.copy()

    return cleaned