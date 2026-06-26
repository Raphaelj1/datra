def calculate_score(results: dict):
    scores = {}
    
    comp = results.get("completeness", {})
    if comp:
        ratios = [
            v["completeness_ratio"]
            for v in comp.values()
        ]
        scores["completeness"] = (
            sum(ratios) / len(ratios)
            if ratios
            else 0
        )
    else:
        scores["completeness"] = 0


    # lower duplicates = better
    uniq = results.get("uniqueness", {})
    if uniq:
        dup_ratio = uniq.get("duplicate_ratio", 1)
        scores["uniqueness"] = 1 - dup_ratio
    else:
        scores["uniqueness"] = 0


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
    

    overall_score = round(
        sum(scores.values()) / len(scores),
        2
    )

    return {
        "scores": { 
            k: round(v, 2)
            for k, v in scores.items()
        },
        "overall_score": overall_score,
    }