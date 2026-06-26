import pandas as pd


def remove_duplicates(df: pd.DataFrame):

    return df.drop_duplicates().copy()