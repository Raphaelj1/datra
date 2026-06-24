import pandas as pd


def plausibility(df: pd.DataFrame):
    issues = {}

    for col in df.columns:
        col_data = df[col]

        col_issues = []

        if pd.api.types.is_numeric_dtype(col_data):

            if (col_data < 0).any():
                col_issues.append("contains negative values")

            if col_data.max() > 120:
                col_issues.append("contains unusually large values (>120)")

        if pd.api.types.is_string_dtype(col_data):

            invalid_strings = col_data.dropna().astype(str).str.lower().isin(
                ["unknown", "none", "n/a", "null"]
            ).sum()

            if invalid_strings > 0:
                col_issues.append(f"{invalid_strings} placeholder values found")

        if col_issues:
            issues[col] = col_issues

    return {
        "total_columns": len(df.columns),
        "columns_with_issues": len(issues),
        "issues": issues
    }