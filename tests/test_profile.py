from datra.checks.profile import profile


def test_profile_returns_dictionary(sample_df):
    result = profile(sample_df)

    assert isinstance(result, dict)


def test_profile_contains_expected_keys(sample_df):
    result = profile(sample_df)

    expected = {
        "rows",
        "columns",
        "numeric_columns",
        "categorical_columns",
        "datetime_columns",
        "memory_usage_mb",
    }

    assert expected.issubset(result.keys())


def test_profile_row_count(sample_df):
    result = profile(sample_df)

    assert result["rows"] == len(sample_df)


def test_profile_column_count(sample_df):
    result = profile(sample_df)

    assert result["columns"] == len(sample_df.columns)


def test_memory_usage_is_numeric(sample_df):
    result = profile(sample_df)

    assert isinstance(result["memory_usage_mb"], float)