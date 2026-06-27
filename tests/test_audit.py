from datra import Audit


def test_create_audit(sample_df):
    audit = Audit(sample_df)

    assert audit.df.equals(sample_df)
    assert audit.df is not sample_df


def test_profile(sample_df):
    audit = Audit(sample_df)

    profile = audit.profile

    assert "rows" in profile
    assert "columns" in profile


def test_completeness(sample_df):
    audit = Audit(sample_df)

    result = audit.completeness

    assert "Age" in result


def test_uniqueness(sample_df):
    audit = Audit(sample_df)

    result = audit.uniqueness

    assert "duplicate_rows" in result


def test_outliers(sample_df):
    audit = Audit(sample_df)

    result = audit.outliers

    assert isinstance(result, dict)


def test_score(sample_df):
    audit = Audit(sample_df)

    score = audit.score

    assert "overall_score" in score
    assert "scores" in score


def test_results(sample_df):
    audit = Audit(sample_df)

    results = audit.results

    expected = {
        "profile",
        "completeness",
        "uniqueness",
        "outliers",
        "score",
    }

    assert expected.issubset(results.keys())


def test_build_report(sample_df):
    audit = Audit(sample_df)

    report = audit.build_report()

    assert "metadata" in report
    assert "summary" in report


def test_save_report(sample_df, tmp_path):
    audit = Audit(sample_df)

    path = audit.save_report(
        path=tmp_path,
        format="json",
    )

    assert path.exists()