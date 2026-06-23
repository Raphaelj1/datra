def calculate_score(results: dict):
    """
    results = {
        "completeness": {...},
        "uniqueness": {...},
        "plausibility": {...},
        "outliers": {...}
    }
    """

    scores = {}


    comp = results.get("completeness", {})
    if comp:
        ratios = [
            v["completeness_ratio"]
            for v in comp.values()
        ]
        scores["completeness"] = sum(ratios) / len(ratios)
    else:
        scores["completeness"] = 0


    # lower duplicates = better
    uniq = results.get("uniqueness", {})
    if uniq:
        dup_ratio = uniq.get("duplicate_ratio", 1)
        scores["uniqueness"] = 1 - dup_ratio
    else:
        scores["uniqueness"] = 0


    # fewer issues = better
    plaus = results.get("plausibility", {})
    if plaus:
        total_cols = plaus.get("total_columns", 0)
        bad_cols = plaus.get("columns_with_issues", 0)

        scores["plausibility"] = 1 - (bad_cols / total_cols) if total_cols else 0
    else:
        scores["plausibility"] = 0


    out = results.get("outliers", {})
    if out:
        ratios = [
            v["outlier_ratio"]
            for v in out.values()
        ]
        avg_outlier = sum(ratios) / len(ratios)
        scores["outliers"] = 1 - avg_outlier
    else:
        scores["outliers"] = 1

    # weighted final score
    final = (
        scores["completeness"] * 0.30 +
        scores["uniqueness"] * 0.20 +
        scores["plausibility"] * 0.25 +
        scores["outliers"] * 0.25
    )

    return {
        "scores": {
            k: round(v * 100, 2)
            for k, v in scores.items()
        },
        "final_score": round(final * 100, 2)
    }