from datetime import datetime
import os

from config import config

from logger import logger

os.makedirs("output", exist_ok=True)


def generate_validation_report(
    total_rows,
    passed_rows,
    failed_rows,
    date_errors,
    amount_errors,
    store_errors
):

    report = f"""
==========================================
ETL VALIDATION REPORT
==========================================

Run Time      : {datetime.now()}

Rows Extracted: {total_rows}
Rows Passed   : {passed_rows}
Rows Failed   : {failed_rows}

Validation Breakdown
------------------------------------------

Date Errors   : {date_errors}
Amount Errors : {amount_errors}
Store Errors  : {store_errors}

Success Rate  : {(passed_rows / total_rows) * 100:.2f}%

==========================================
"""

    with open(
        config["validation_report"],
        "w"
    ) as file:

        file.write(report)

    logger.info(f"Validation report generated")