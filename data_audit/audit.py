import pandas as pd
from pathlib import Path
from data_audit.checks.completeness import completeness
from data_audit.checks.uniqueness import uniqueness
from data_audit.checks.plausibility import plausibility
from data_audit.checks.outliers import outliers
from data_audit.checks.profile import profile
from data_audit.reports.score_calculator import calculate_score
from data_audit.reports.report_builder import build_report, save_report

class DataAudit:
    def __init__(self, input_data):
        self.df = self._resolve_input(input_data)
        self.results = {}

        
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
    
    
    def completeness(self):
        result = completeness(self.df)
        self.results["completeness"] = result
        return result
    
    def uniqueness(self):
        result = uniqueness(self.df)
        self.results["uniqueness"] = result
        return result
    
    
    def plausibility(self):
        result = plausibility(self.df)
        self.results["plausibility"] = result
        return result
    
    
    def outliers(self):
        result = outliers(self.df)
        self.results["outliers"] = result
        return result
    
    
    def score(self):
        if "score" not in self.results:
            if "completeness" not in self.results:
                self.completeness()
            if "uniqueness" not in self.results:
                self.uniqueness()
            if "plausibility" not in self.results:
                self.plausibility()
            if "outliers" not in self.results:
                self.outliers()

            self.results["score"] = calculate_score(self.results)

        return self.results["score"]
    
    
    def profile(self):
        result = profile(self.df)
        self.results["profile"] = result
        return result
    

    def build_report(self, format="json"):
        if "profile" not in self.results:
            self.profile()
            
        if "score" not in self.results:
            self.score()

        return build_report(self.results, format=format)


    def save_report(self, path="reports", format="json"):
        report = self.build_report(format=format)
        return save_report(report, path=path, format=format)