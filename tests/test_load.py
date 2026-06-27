import pytest
from pathlib import Path

from datra.io import load


def test_load_dataframe(sample_df):
    loaded = load(sample_df)

    assert loaded.equals(sample_df)
    assert loaded is not sample_df


def test_invalid_input():
    with pytest.raises(TypeError):
        load(123)


def test_load_csv(sample_df, tmp_path):
    path = tmp_path / "patients.csv"

    sample_df.to_csv(path, index=False)

    loaded = load(path)

    assert loaded.shape == sample_df.shape
    assert list(loaded.columns) == list(sample_df.columns)


def test_load_excel(sample_df, tmp_path):
    path = tmp_path / "patients.xlsx"

    sample_df.to_excel(path, index=False)

    loaded = load(path)

    assert loaded.shape == sample_df.shape
    assert list(loaded.columns) == list(sample_df.columns)


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load(Path("does_not_exist.csv"))


def test_unsupported_file_type(tmp_path):
    path = tmp_path / "patients.txt"

    path.write_text("hello")

    with pytest.raises(ValueError):
        load(path)