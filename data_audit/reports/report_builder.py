import json
from datetime import datetime
from pathlib import Path


def build_report(results: dict, format="json"):
    report = {
        "metadata": {
            "generated_at": datetime.now().isoformat(),
            "tool": "data-audit"
        },

        "summary": _build_summary(results),

        "profile": results.get("profile", {}),

        "checks": {
            "completeness": results.get("completeness", {}),
            "uniqueness": results.get("uniqueness", {}),
            "plausibility": results.get("plausibility", {}),
            "outliers": results.get("outliers", {})
        },

        "score": results.get("score", {})
    }

    if format == "json":
        return report

    if format == "html":
        return _to_html(report)

    raise ValueError(f"Unsupported format: {format}")


def _build_summary(results: dict):
    score = results.get("score", {}).get("final_score", None)

    return {
        "dataset_quality_score": score,
        "has_completeness_issues": bool(results.get("completeness")),
        "has_duplicates": bool(results.get("uniqueness", {}).get("duplicate_rows", 0)),
        "has_outliers": bool(results.get("outliers")),
        "columns_analyzed": len(results.get("profile", {}).get("columns", {}))
    }
    

def _to_html(report: dict):
    html = f"""
    <html>
    <head><title>Data Audit Report</title></head>
    <body>
        <h1>Data Quality Report</h1>

        <h2>Summary</h2>
        <pre>{report['summary']}</pre>

        <h2>Score</h2>
        <pre>{report['score']}</pre>

        <h2>Checks</h2>
        <pre>{report['checks']}</pre>
    </body>
    </html>
    """

    return html


def save_report(report: dict, path: str = "reports", format: str = "json"):
    output_dir = Path(path)
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if format == "json":
        file_path = output_dir / f"data_audit_report_{timestamp}.json"

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)

        return str(file_path)

    if format == "html":
        file_path = output_dir / f"data_audit_report_{timestamp}.html"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(_to_html(report))

        return str(file_path)

    raise ValueError(f"Unsupported format: {format}")