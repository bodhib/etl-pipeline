import pandas as pd

from validations.date_rules import validate_date
from validations.amount_rules import validate_amount
from validations.store_rules import validate_store


def run_validations(df):

    total_rows = len(df)

    failed_records = []

    current_df = df.copy()

    current_df, failed, date_errors = validate_date(
        current_df
    )
    failed_records.append(failed)

    current_df, failed, amount_errors = validate_amount(
        current_df
    )
    failed_records.append(failed)

    current_df, failed, store_errors = validate_store(
        current_df
    )
    failed_records.append(failed)

    failed_df = pd.concat(
        failed_records,
        ignore_index=True
    )

    passed_rows = len(current_df)

    failed_rows = len(failed_df)

    stats = {
        "total_rows": total_rows,
        "passed_rows": passed_rows,
        "failed_rows": failed_rows,
        "date_errors": date_errors,
        "amount_errors": amount_errors,
        "store_errors": store_errors
    }

    return current_df, failed_df, stats