def validate_amount(df):

    failed = df[
        df["amount"] <= 0
    ]

    passed = df[
        df["amount"] > 0
    ]

    return passed, failed, len(failed)