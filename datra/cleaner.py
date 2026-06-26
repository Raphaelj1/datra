from copy import deepcopy

from datra.defaults import DEFAULT_CLEANING_RULES
from datra.cleaning.duplicates import remove_duplicates
from datra.cleaning.missing import fill_missing


def clean(df, rules=None, **kwargs):
    if rules is not None and kwargs:
        raise ValueError(
            "Cannot use both 'rules' and keyword arguments."
        )

    if rules is None:
        rules = _kwargs_to_rules(kwargs)

    cleaned = df.copy()

    duplicates = rules.get("duplicates", {})

    if duplicates.get("drop"):
        cleaned = remove_duplicates(cleaned)

    missing = rules.get("missing", {})

    if any(value is not None for value in missing.values()):
        cleaned = fill_missing(cleaned, missing)

    return cleaned


def _kwargs_to_rules(kwargs):
    rules = deepcopy(DEFAULT_CLEANING_RULES)

    if "drop_duplicates" in kwargs:
        rules["duplicates"]["drop"] = kwargs["drop_duplicates"]

    if "fill_numeric" in kwargs:
        rules["missing"]["numeric"] = kwargs["fill_numeric"]

    if "fill_categorical" in kwargs:
        rules["missing"]["categorical"] = kwargs["fill_categorical"]

    return rules