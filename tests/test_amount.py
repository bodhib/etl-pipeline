import pandas as pd

from validations.amount_rules import validate_amount


def test_amount_validation():

    df = pd.DataFrame({
        "amount": [100, -50]
    })

    passed, failed, count = validate_amount(df)

    assert len(passed) == 1
    assert len(failed) == 1