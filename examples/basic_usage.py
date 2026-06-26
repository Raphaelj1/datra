from pathlib import Path
import pandas as pd
from datra import DataAudit, clean

file_path = Path(__file__).parent / "patients.csv"

audit = DataAudit(file_path)

# print(audit.completeness)
# print(audit.uniqueness)
# print(audit.plausibility)
# print(audit.outliers)
# print(audit.score)
# print(audit.profile)

# audit.save_report(path="reports")

# df = pd.DataFrame({
#     "name": ["A", "A"],
#     "age": [20, 20]
# })

# cleaned_df, report = clean(df, {})

# print(cleaned_df)
# print(report)

# rules = {
#   "duplicates": {
#     "drop": False
#   }
# }

df = pd.read_csv(file_path)

clean_df = clean(df)

clean_df.to_csv("examples/output.csv", index=False)
