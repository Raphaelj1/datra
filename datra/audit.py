from functools import cached_property
import pandas as pd
from pathlib import Path

from datra.io import load

from datra.checks.validate import validate as validate_df
from datra.checks.completeness import completeness as check_completeness
from datra.checks.uniqueness import uniqueness as check_uniqueness
from datra.checks.outliers import outliers as check_outliers
from datra.checks.profile import profile as check_profile
from datra.reports.score_calculator import calculate_score
from datra.reports.report_builder import build_report, save_report

class DataAudit:
    def __init__(self, input_data):
        self.df = load(input_data)
    
    @cached_property
    def completeness(self):
        return check_completeness(self.df)

    @cached_property
    def uniqueness(self):
        return check_uniqueness(self.df)

    @cached_property
    def outliers(self):
        return check_outliers(self.df)

    @cached_property
    def profile(self):
        return check_profile(self.df)

    @cached_property
    def score(self):
        metrics_payload = {
            "completeness": self.completeness,
            "uniqueness": self.uniqueness,
            "outliers": self.outliers,
        }
        return calculate_score(metrics_payload)

    @property
    def results(self):
        return {
            "profile": self.profile,
            "completeness": self.completeness,
            "uniqueness": self.uniqueness,
            "outliers": self.outliers,
            "score": self.score,
        }

    def validate(self, rules: dict):
        return validate_df(self.df, rules)

    def build_report(self, format="json"):
        return build_report(self.results, format=format)

    def save_report(self, path="reports", format="json"):
        report = self.build_report(format=format)
        return save_report(report, path=path, format=format)