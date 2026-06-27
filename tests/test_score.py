from datra.scoring.score import calculate_score


def test_returns_dictionary():
    results = {
        "completeness": {},
        "uniqueness": {},
        "outliers": {},
    }

    score = calculate_score(results)

    assert isinstance(score, dict)


def test_contains_expected_keys():
    results = {
        "completeness": {},
        "uniqueness": {},
        "outliers": {},
    }

    score = calculate_score(results)

    expected = {
        "scores",
        "overall_score",
    }

    assert expected == set(score.keys())


def test_overall_score_is_numeric():
    results = {
        "completeness": {},
        "uniqueness": {},
        "outliers": {},
    }

    score = calculate_score(results)

    assert isinstance(score["overall_score"], (int, float))


def test_perfect_dataset_scores_100_percent():
    results = {
        "completeness": {
            "Age": {
                "completeness_ratio": 1.0
            }
        },
        "uniqueness": {
            "duplicate_ratio": 0
        },
        "outliers": {
            "Age": {
                "outlier_ratio": 0
            }
        },
    }

    score = calculate_score(results)

    assert score["overall_score"] == 1.0


def test_score_is_between_zero_and_one():
    results = {
        "completeness": {
            "Age": {
                "completeness_ratio": 0.5
            }
        },
        "uniqueness": {
            "duplicate_ratio": 0.2
        },
        "outliers": {
            "Age": {
                "outlier_ratio": 0.1
            }
        },
    }

    score = calculate_score(results)

    assert 0 <= score["overall_score"] <= 1