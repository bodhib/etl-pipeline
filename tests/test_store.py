import pandas as pd

from validations.store_rules import validate_store


def test_store_validation():

    df = pd.DataFrame({
        "store_name": ["Kolkata", None]
    })

    passed, failed, count = validate_store(df)

    assert len(passed) == 1
    assert len(failed) == 1