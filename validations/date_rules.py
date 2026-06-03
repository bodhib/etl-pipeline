import pandas as pd


def validate_date(df):

    df = df.copy()

    df["sales_date"] = pd.to_datetime(
        df["sales_date"],
        errors="coerce"
    )

    failed = df[
        df["sales_date"].isna()
    ]

    passed = df[
        df["sales_date"].notna()
    ]

    return passed, failed, len(failed)