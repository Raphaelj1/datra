import pandas as pd


def _fill_numeric(df: pd.DataFrame, strategy):
    numeric_columns = df.select_dtypes(include="number").columns

    if numeric_columns.empty:
        return df
    
    if strategy == "zero":
        value = 0

    elif strategy in ("mean", "median"):
        value = df[numeric_columns].agg(strategy)

    elif strategy == "mode":
        mode_df = df[numeric_columns].mode()
        value = mode_df.iloc[0] if not mode_df.empty else pd.Series(dtype="float64")


    else: 
        raise ValueError(f"Unknown numeric strategy '{strategy}'. Use 'mean', 'median', 'mode', or 'zero'.")

    df[numeric_columns] = df[numeric_columns].fillna(value)



def _fill_categorical(df: pd.DataFrame, strategy):
    categorical_columns = df.select_dtypes(exclude="number").columns

    if categorical_columns.empty:
        return df
    
    if strategy == "mode":
        mode_df = df[categorical_columns].mode()
        value = mode_df.iloc[0] if not mode_df.empty else pd.Series(dtype="object")

    else: 
        raise ValueError(f"Unknown categorical strategy '{strategy}'. Use 'mode'.")

    df[categorical_columns] = df[categorical_columns].fillna(value)


def fill_missing(df: pd.DataFrame, rules: dict) -> pd.DataFrame:
    cleaned = df.copy()

    numeric_strategy = rules.get("numeric")
    categorical_strategy = rules.get("categorical")

    if numeric_strategy:
        _fill_numeric(cleaned, numeric_strategy)

    if categorical_strategy:
        _fill_categorical(cleaned, categorical_strategy)

    return cleaned