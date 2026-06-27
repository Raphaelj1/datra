import pandas as pd
import pytest


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "Patient ID": [1, 2, 2, 4, 5, 5, 5],
            "Age": [20, None, 30, 500, None, None, None],
            "Gender": ["Male", "Female", None, "Male", "Female", "Female", "Female"],
        }
    )

