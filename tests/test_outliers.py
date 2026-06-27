import pytest

from datra.checks.outliers import outliers


def test_returns_dictionary(sample_df):
    result = outliers(sample_df)

    assert isinstance(result, dict)


def test_numeric_column_is_checked(sample_df):
    result = outliers(sample_df)

    assert "Age" in result


def test_contains_expected_keys(sample_df):
    age = outliers(sample_df)["Age"]

    expected = {
        "outlier_count",
        "outlier_ratio",
        "lower_bound",
        "upper_bound",
    }

    assert expected == set(age.keys())


def test_bounds_are_numeric(sample_df):
    age = outliers(sample_df)["Age"]

    assert isinstance(age["lower_bound"], (int, float))
    assert isinstance(age["upper_bound"], (int, float))


def test_outlier_ratio_matches_count(sample_df):
    age = outliers(sample_df)["Age"]

    non_null = sample_df["Age"].notna().sum()

    expected = age["outlier_count"] / non_null

    assert age["outlier_ratio"] == pytest.approx(round(expected, 4))