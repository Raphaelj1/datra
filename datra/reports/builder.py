from datetime import datetime


def build_report(results: dict):
    return {
        "metadata": {
            "generated_at": datetime.now().isoformat(),
            "tool": "datra",
        },

        "summary": _build_summary(results),

        "profile": results.get("profile", {}),

        "checks": {
            "completeness": results.get("completeness", {}),
            "uniqueness": results.get("uniqueness", {}),
            "outliers": results.get("outliers", {}),
        },

        "score": results.get("score", {}),
    }


def _build_summary(results: dict):
    score = results.get("score", {})

    return {
        "dataset_quality_score": score.get("overall_score"),
        "rows": results.get("profile", {}).get("rows"),
        "columns": results.get("profile", {}).get("columns"),
        "has_duplicates": bool(results.get("uniqueness", {}).get("duplicate_rows", 0)),
        "has_missing_values": bool(results.get("completeness")),
        "has_outliers": bool(results.get("outliers")),
    }
