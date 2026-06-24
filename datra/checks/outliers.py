import pandas as pd


def outliers(df: pd.DataFrame):
    results = {}

    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        series = df[col].dropna()

        if series.empty:
            continue

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers_mask = (series < lower_bound) | (series > upper_bound)

        outlier_values = series[outliers_mask]

        results[col] = {
            "lower_bound": float(lower_bound),
            "upper_bound": float(upper_bound),
            "outlier_count": int(outliers_mask.sum()),
            "outlier_ratio": float(round(outliers_mask.mean(), 4)),
            # "sample_outliers": outlier_values.head(5).tolist()
        }

    return results