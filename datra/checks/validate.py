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
        
        
def _check_minimum(df, column, minimum, summary, column_result):
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
        

def _check_maximum(df, column, maximum, summary, column_result):
    violations = int((df[column] > maximum).sum())

    passed = violations == 0

    _record_check(
        summary,
        column_result,
        "maximum",
        passed,
        expected=maximum,
        violations=violations,
    )


def _check_allowed(df, column, allowed, summary, column_result):
    violations = int(
        (~df[column].isin(allowed)).sum()
    )

    passed = violations == 0

    _record_check(
        summary,
        column_result,
        "allowed",
        passed,
        expected=allowed,
        violations=violations,
    )


def _check_unique(df, column, summary, column_result):
    violations = int(df[column].duplicated().sum())

    passed = violations == 0

    _record_check(
        summary,
        column_result,
        "unique",
        passed,
        violations=violations,
    )


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
        
        if "min" in column_rules:
            _check_minimum(
                df,
                column,
                column_rules["min"],
                summary,
                column_result,
            )

        if "max" in column_rules:
            _check_maximum(
                df,
                column,
                column_rules["max"],
                summary,
                column_result,
            )

        if "allowed" in column_rules:
            _check_allowed(
                df,
                column,
                column_rules["allowed"],
                summary,
                column_result,
            )

        if column_rules.get("unique"):
            _check_unique(
                df,
                column,
                summary,
                column_result,
            )

        results[column] = column_result
                
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