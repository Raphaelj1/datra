from datra.reports.builder import build_report


def sample_results():
    return {
        "profile": {
            "rows": 7,
            "columns": 3,
        },
        "completeness": {},
        "uniqueness": {
            "total_rows": 7,
            "duplicate_rows": 2,
            "duplicate_ratio": 0.2857,
        },
        "outliers": {},
        "score": {
            "scores": {
                "completeness": 0.9,
                "uniqueness": 0.8,
                "outliers": 1.0,
            },
            "overall_score": 0.9,
        },
    }


def test_returns_dictionary():
    report = build_report(sample_results())

    assert isinstance(report, dict)


def test_contains_expected_sections():
    report = build_report(sample_results())

    expected = {
        "metadata",
        "summary",
        "profile",
        "checks",
        "score",
    }

    assert expected == set(report.keys())


def test_metadata_exists():
    report = build_report(sample_results())

    metadata = report["metadata"]

    assert "generated_at" in metadata
    assert "tool" in metadata


def test_summary_exists():
    report = build_report(sample_results())

    assert isinstance(report["summary"], dict)


def test_checks_contains_expected_sections():
    report = build_report(sample_results())

    expected = {
        "completeness",
        "uniqueness",
        "outliers",
    }

    assert expected == set(report["checks"].keys())