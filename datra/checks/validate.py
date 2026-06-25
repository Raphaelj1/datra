import pandas as pd


def _record_check(summary, column_result, check_name, passed, **details):
    column_result["checks"][check_name] = {
        "passed": passed,
        **details,
    }

    summary["rules_checked"] += 1

    if passed:
        summary["rules_passed"] += 1
    else:
        summary["rules_failed"] += 1
        column_result["passed"] = False
        

def validate(df: pd.DataFrame, rules: dict):
    summary = {
        "columns_checked": 0,
        "rules_checked": 0,
        "rules_passed": 0,
        "rules_failed": 0,
        "validation_score": 0.0,
    }

    results = {}

    for column, column_rules in rules.items():
        if column not in df.columns:
            continue

        summary["columns_checked"] += 1

        column_result = {
            "passed": True,
            "checks": {}
        }

        results[column] = column_result
        
        if "min" in column_rules:
            minimum = column_rules["min"]

            violations = int((df[column] < minimum).sum())

            passed = violations == 0

            _record_check(
                summary,
                column_result,
                "minimum",
                passed,
                expected=minimum,
                violations=violations,
            )
        
        if "max" in column_rules:
            maximum = column_rules["max"]

            violations = int((df[column] > maximum).sum())

            passed = violations == 0

            _record_check(
                summary,
                column_result,
                "minimum",
                passed,
                expected=minimum,
                violations=violations,
            )
                
                
        if "allowed" in column_rules:
            allowed = column_rules["allowed"]

            violations = int(
                (~df[column].isin(allowed)).sum()
            )

            passed = violations == 0

            _record_check(
                summary,
                column_result,
                "minimum",
                passed,
                expected=minimum,
                violations=violations,
            )
                
        if column_rules.get("unique"):
            violations = int(df[column].duplicated().sum())

            passed = violations == 0

            _record_check(
                summary,
                column_result,
                "minimum",
                passed,
                expected=minimum,
                violations=violations,
            )
                
        if summary["rules_checked"]:
            summary["validation_score"] = round(
                (
                    summary["rules_passed"]
                    / summary["rules_checked"]
                ) * 100,
                2,
            )

    return {
        "summary": summary,
        "columns": results,
    }