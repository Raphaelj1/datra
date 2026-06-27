import pandas as pd

from datra import clean


def test_returns_new_dataframe(sample_df):
    cleaned = clean(sample_df)

    assert cleaned is not sample_df


def test_drop_duplicates(sample_df):
    cleaned = clean(
        sample_df,
        drop_duplicates=True,
    )

    assert cleaned.duplicated().sum() == 0


def test_fill_numeric(sample_df):
    cleaned = clean(
        sample_df,
        fill_numeric="median",
    )

    assert cleaned["age"].isna().sum() == 0


def test_fill_categorical(sample_df):
    cleaned = clean(
        sample_df,
        fill_categorical="mode",
    )

    assert cleaned["gender"].isna().sum() == 0


def test_standardize_columns(sample_df):
    cleaned = clean(
        sample_df,
        standardize_columns=True,
    )

    assert "patient_id" in cleaned.columns


def test_save_cleaned_dataframe(sample_df, tmp_path):
    output = tmp_path / "clean.csv"

    cleaned = clean(
        sample_df,
        output=output,
    )

    assert output.exists()
    assert isinstance(cleaned, pd.DataFrame)


def test_clean_with_rules(sample_df):
    rules = {
        "duplicates": {
            "drop": True
        },
        "columns": {
            "standardize": True
        }
    }

    cleaned = clean(
        sample_df,
        rules=rules,
    )

    assert "patient_id" in cleaned.columns


def test_keyword_arguments_override_rules(sample_df):
    rules = {
        "duplicates": {
            "drop": False
        }
    }

    cleaned = clean(
        sample_df,
        rules=rules,
        drop_duplicates=True,
    )

    assert cleaned.duplicated().sum() == 0


