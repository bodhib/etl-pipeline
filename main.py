from extract import extract_data
from transform import transform_data
from load import load_data
from logger import logger
from fetch_data import fetch_data

from validations.validation_engine import run_validations

from report_generator import (
    generate_validation_report
)

from audit import (
    create_audit_table,
    insert_audit_record
)

from config import config

import sys

INPUT_FILE = config["input_file"]

try:

    logger.info("ETL pipeline started")

    # create audit table if not exists
    create_audit_table()

    # Extract
    raw_df = extract_data(INPUT_FILE)

    validated_df, failed_df, stats = run_validations(
        raw_df
    )
    # print(validated_df)
    # sys.exit(0)

    # Log failed records
    failed_df.to_csv(
        config["failed_records"],
        index=False
    )

    # Generate validation report
    generate_validation_report(
        stats["total_rows"],
        stats["passed_rows"],
        stats["failed_rows"],
        stats["date_errors"],
        stats["amount_errors"],
        stats["store_errors"]
    )

    # insert audit record
    insert_audit_record(
        stats["total_rows"],
        stats["passed_rows"],
        stats["failed_rows"],
        stats["date_errors"],
        stats["amount_errors"],
        stats["store_errors"],
        "SUCCESS"
    )

    # Transform
    transform_df = transform_data(validated_df)

    # Load
    load_data(transform_df)

    logger.info("ETL pipeline completed successfully")

    # Fetch data to verify ETL pipeline completion
    fetch_data()

except Exception as e:

    logger.error(f"ETL pipeline failed: {str(e)}")

    raise