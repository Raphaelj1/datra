from datra.checks.completeness import completeness


def test_returns_dictionary(sample_df):
    result = completeness(sample_df)

    assert isinstance(result, dict)


def test_contains_columns_with_missing_values(sample_df):
    result = completeness(sample_df)

    assert "Age" in result
    assert "Gender" in result


def test_age_statistics(sample_df):
    result = completeness(sample_df)

    print(result)

    age = result["Age"]

    assert age["missing_values"] == 4
    assert age["completeness_ratio"] == 0.4286


def test_gender_statistics(sample_df):
    result = completeness(sample_df)

    gender = result["Gender"]

    assert gender["missing_values"] == 1
    assert gender["completeness_ratio"] == 0.8571


def test_complete_columns_have_no_missing_values(sample_df):
    result = completeness(sample_df)

    patient_id = result["Patient ID"]

    assert patient_id["missing_values"] == 0
    assert patient_id["completeness_ratio"] == 1.0