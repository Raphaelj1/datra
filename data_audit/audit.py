import pandas as pd
from pathlib import Path
from data_audit.checks.completeness import completeness

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