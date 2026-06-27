# Datra

A lightweight Python library for cleaning, auditing, and validating tabular data. It helps data scientists, analysts, and engineers quickly identify data quality issues, clean datasets using simple rules, and generate reports.

## Why Datra?

Data quality problems often consume more time than analysis itself. Missing values, duplicate records, inconsistent column names, and invalid entries can silently affect downstream models and business decisions.

Datra provides a simple workflow for understanding and improving dataset quality before analysis or machine learning.

With Datra, you can:

- Audit datasets to identify quality issues.
- Clean data using configurable rules.
- Validate datasets against business rules.
- Generate JSON and HTML quality reports.
- Work directly with Pandas DataFrames or CSV and Excel files.

## Features

- Dataset profiling
- Missing value analysis
- Duplicate detection
- Outlier detection (IQR-based)
- Rule-based data validation
- Automated data quality scoring
- Configurable data cleaning
- Column name standardization
- Support for Pandas DataFrames
- CSV and Excel file support
- JSON and HTML report generation
- Save cleaned datasets directly to disk

## Installation

Install Datra from PyPI:

```bash
pip install datra
```

Or install the latest development version:

```bash
git clone https://github.com/raphaelj1/datra.git

cd datra

pip install -e .
```

## Quick Start

### Clean a dataset

```python
from datra import clean

cleaned = clean(
    "patients.csv",
    drop_duplicates=True,
    fill_numeric="median",
    fill_categorical="mode",
    standardize_columns=True,
)
```

### Audit a dataset

```python
from datra import Audit

audit = Audit("patients.csv")

print(audit.profile)
print(audit.score)
```

### Validate a dataset

```python
rules = {
    "Age": {
        "min": 0,
        "max": 120,
    },
    "Gender": {
        "allowed": [
            "Male",
            "Female",
        ],
    },
}

report = audit.validate(rules)
```

## Cleaning Data

The `clean()` function applies one or more cleaning operations to a dataset and returns a new DataFrame. It accepts either a Pandas DataFrame or the path to a CSV or Excel file.

### Using keyword arguments

```python
from datra import clean

cleaned = clean(
    "patients.csv",
    drop_duplicates=True,
    fill_numeric="median",
    fill_categorical="mode",
    standardize_columns=True,
)
```

### Using cleaning rules

```python
rules = {
    "duplicates": {
        "drop": True,
    },
    "missing": {
        "numeric": "median",
        "categorical": "mode",
    },
    "columns": {
        "standardize": True,
    },
}

cleaned = clean("patients.csv", rules=rules)
```

### Save the cleaned dataset

```python
clean(
    "patients.csv",
    drop_duplicates=True,
    output="cleaned_patients.xlsx",
)
```

## Auditing Data

Create an audit object to inspect dataset quality.

```python
from datra import Audit

audit = Audit("patients.csv")
```

Retrieve individual quality checks.

```python
audit.profile

audit.completeness

audit.uniqueness

audit.outliers

audit.score
```

Or access all audit results at once.

```python
audit.results
```

## Validation

Validate datasets against custom business rules.

```python
rules = {
    "Age": {
        "min": 0,
        "max": 120,
    },
    "Patient ID": {
        "unique": True,
    },
    "Gender": {
        "allowed": [
            "Male",
            "Female",
        ],
    },
}

report = audit.validate(rules)
```

Validation returns a structured report describing which checks passed, which failed, and the number of violations for each rule.

## Reports

Build a data quality report as a Python dictionary.

```python
from datra import Audit

audit = Audit("patients.csv")

report = audit.build_report()
```

Save the report as JSON.

```python
audit.save_report(
    format="json",
)
```

Or save it as an HTML report.

```python
audit.save_report(
    format="html",
)
```

## Supported File Formats

Datra supports both Pandas DataFrames and common tabular file formats.

| Input            | Supported |
| ---------------- | --------- |
| Pandas DataFrame | ✅        |
| CSV              | ✅        |
| Excel (.xlsx)    | ✅        |
| Excel (.xls)     | ✅        |

### Report Formats

| Format | Supported  |
| ------ | ---------- |
| JSON   | ✅         |
| HTML   | ✅         |
| PDF    | 🚧 Planned |

## Project Structure

```
datra/
├── datra/              # Library source code
├── examples/           # Example usage
├── tests/
├── pyproject.toml
├── README.md
└── LICENSE
```

## Roadmap

Planned improvements include:

- PDF report generation
- Command-line interface (CLI)
- Additional cleaning operations
- Additional validation rules
- More data quality checks
- Interactive HTML reports
- Support for additional file formats

## Contributing

Contributions, feature requests, and bug reports are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Open a pull request.

Please ensure all tests pass before submitting a pull request.

## License

This project is licensed under the MIT License.
