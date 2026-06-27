import pytest

from datra.checks.uniqueness import uniqueness


def test_returns_dictionary(sample_df):
    result = uniqueness(sample_df)

    assert isinstance(result, dict)


def test_contains_expected_keys(sample_df):
    result = uniqueness(sample_df)

    expected = {
        "total_rows",
        "unique_rows",
        "duplicate_rows",
        "duplicate_ratio",
    }

    assert expected == set(result.keys())


def test_total_rows(sample_df):
    result = uniqueness(sample_df)

    assert result["total_rows"] == len(sample_df)


def test_duplicate_rows(sample_df):
    result = uniqueness(sample_df)

    expected_duplicates = sample_df.duplicated().sum()

    assert result["duplicate_rows"] == expected_duplicates


def test_duplicate_ratio(sample_df):
    result = uniqueness(sample_df)

    print(result)

    expected_ratio = sample_df.duplicated().sum() / len(sample_df)

    assert result["duplicate_ratio"] == pytest.approx(
        round(expected_ratio, 4)
    )