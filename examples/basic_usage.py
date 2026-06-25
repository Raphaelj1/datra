from datra.audit import DataAudit
from pathlib import Path
from datra.cleaner import clean
import pandas as pd

file_path = Path(__file__).parent / "patients.csv"

audit = DataAudit(file_path)

# print(audit.completeness)
# print(audit.uniqueness)
# print(audit.plausibility)
# print(audit.outliers)
# print(audit.score)
# print(audit.profile)

# audit.save_report(path="reports")

df = pd.DataFrame({
    "name": ["A", "A"],
    "age": [20, 20]
})

cleaned_df, report = clean(df, {})

print(cleaned_df)
print(report)