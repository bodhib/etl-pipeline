def validate_store(df):

    failed = df[
        df["store_name"].isna()
    ]

    passed = df[
        df["store_name"].notna()
    ]

    return passed, failed, len(failed)