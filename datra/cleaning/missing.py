import pandas as pd


def _fill_numeric(df, strategy):
    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:

        if strategy == "mean":
            value = df[column].mean()

        elif strategy == "median":
            value = df[column].median()

        elif strategy == "mode":
            value = df[column].mode().iloc[0]

        else:
            continue

        df[column] = df[column].fillna(value)



def _fill_categorical(df, strategy):
    categorical_columns = df.select_dtypes(exclude="number").columns

    for column in categorical_columns:

        if strategy == "mode":
            value = df[column].mode().iloc[0]

        else:
            continue

        df[column] = df[column].fillna(value)


def fill_missing(df: pd.DataFrame, rules: dict):
    cleaned = df.copy()

    numeric_strategy = rules.get("numeric")
    categorical_strategy = rules.get("categorical")

    if numeric_strategy:
        _fill_numeric(cleaned, numeric_strategy)

    if categorical_strategy:
        _fill_categorical(cleaned, categorical_strategy)

    return cleaned