from data_audit.audit import DataAudit
from pathlib import Path

file_path = Path(__file__).parent / "patients.csv"

audit = DataAudit(file_path)

# print(audit.completeness())
# print(audit.uniqueness())
# print(audit.plausibility())
# print(audit.outliers())
# print(audit.score())
# print(audit.profile())

print(audit.save_report(format="json"))
