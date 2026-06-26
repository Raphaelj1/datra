from copy import deepcopy

from datra.io import load, save
from datra.defaults import DEFAULT_CLEANING_RULES
from datra.cleaning.duplicates import remove_duplicates
from datra.cleaning.missing import fill_missing
from datra.cleaning.columns import standardize_column_names


def clean(
    data,
    *,
    rules=None,
    drop_duplicates=None,
    fill_numeric=None,
    fill_categorical=None,
    standardize_columns=None,
    output=None,
    format=None,
):
    df = load(data)

    rules = _build_rules(
            rules,
            drop_duplicates=drop_duplicates,
            fill_numeric=fill_numeric,
            fill_categorical=fill_categorical,
            standardize_columns=standardize_columns,
        )

    cleaned = df.copy()

    if rules["duplicates"]["drop"]:
        cleaned = remove_duplicates(cleaned)

    missing = rules["missing"]
    if any(value is not None for value in missing.values()):
        cleaned = fill_missing(cleaned, missing)

    if rules["columns"]["standardize"]:
        cleaned = standardize_column_names(cleaned)

    if output is not None:
        save(cleaned, output, format)

    return cleaned


def _build_rules(
    rules,
    *,
    drop_duplicates,
    fill_numeric,
    fill_categorical,
    standardize_columns,
):
    merged = deepcopy(DEFAULT_CLEANING_RULES)

    if rules is not None:
        merged.update(rules)

    if drop_duplicates is not None:
        merged["duplicates"]["drop"] = drop_duplicates

    if fill_numeric is not None:
        merged["missing"]["numeric"] = fill_numeric

    if fill_categorical is not None:
        merged["missing"]["categorical"] = fill_categorical

    if standardize_columns is not None:
        merged["columns"]["standardize"] = standardize_columns

    return merged