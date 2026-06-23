from data_audit.audit import DataAudit
from pathlib import Path

file_path = Path(__file__).parent / "patients.csv"

audit = DataAudit(file_path)

print(audit.uniqueness())
