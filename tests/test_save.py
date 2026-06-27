import pytest

from datra.io import save


def test_save_csv(sample_df, tmp_path):
    output = tmp_path / "patients.csv"

    path = save(sample_df, output)

    assert path.exists()


def test_save_excel(sample_df, tmp_path):
    output = tmp_path / "patients.xlsx"

    path = save(sample_df, output)

    assert path.exists()


def test_save_with_format(sample_df, tmp_path):
    output = tmp_path / "patients"

    path = save(
        sample_df,
        output,
        format="csv",
    )

    assert path.suffix == ".csv"
    assert path.exists()


def test_unsupported_format(sample_df, tmp_path):
    with pytest.raises(ValueError):
        save(
            sample_df,
            tmp_path / "patients.xyz",
        )


