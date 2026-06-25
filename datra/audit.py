from functools import cached_property
import pandas as pd
from pathlib import Path

from datra.checks.completeness import completeness as check_completeness
from datra.checks.uniqueness import uniqueness as check_uniqueness
from datra.checks.plausibility import plausibility as check_plausibility
from datra.checks.outliers import outliers as check_outliers
from datra.checks.profile import profile as check_profile
from datra.reports.score_calculator import calculate_score
from datra.reports.report_builder import build_report, save_report

class DataAudit:
    def __init__(self, input_data):
        self.df = self._resolve_input(input_data)

        
    def _resolve_input(self, input_data):
        if isinstance(input_data, pd.DataFrame):
            return input_data.copy()

        if isinstance(input_data, (str, Path)):
            path = Path(input_data)

            if not path.exists():
                raise FileNotFoundError(f"File not found: {path}")

            suffix = path.suffix.lower()

            if suffix == ".csv":
                return pd.read_csv(path)

            if suffix in [".xlsx", ".xls"]:
                return pd.read_excel(path)

            raise ValueError(f"Unsupported file type: {suffix}")

        raise ValueError(f"Unsupported input type: {type(input_data)}")
    
    
    @cached_property
    def completeness(self):
        return check_completeness(self.df)

    @cached_property
    def uniqueness(self):
        return check_uniqueness(self.df)

    @cached_property
    def plausibility(self):
        return check_plausibility(self.df)

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
            "plausibility": self.plausibility,
            "outliers": self.outliers,
            "score": self.score,
        }

    def build_report(self, format="json"):
        return build_report(self.results, format=format)

    def save_report(self, path="reports", format="json"):
        report = self.build_report(format=format)
        return save_report(report, path=path, format=format)