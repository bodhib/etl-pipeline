import uuid
from datetime import datetime
import sqlite3

from logger import logger

DATABASE = "database/sales.db"


def create_audit_table():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS etl_audit (

        run_id TEXT PRIMARY KEY,

        execution_time TEXT,

        rows_extracted INTEGER,

        rows_passed INTEGER,

        rows_failed INTEGER,

        date_errors INTEGER,

        amount_errors INTEGER,

        store_errors INTEGER,

        status TEXT

    )
    """)

    conn.commit()

    conn.close()

    logger.info(f"Audit table ready")

def insert_audit_record(
    rows_extracted,
    rows_passed,
    rows_failed,
    date_errors,
    amount_errors,
    store_errors,
    status
):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    run_id = str(uuid.uuid4())

    execution_time = str(datetime.now())

    cursor.execute("""
    INSERT INTO etl_audit (

        run_id,
        execution_time,
        rows_extracted,
        rows_passed,
        rows_failed,
        date_errors,
        amount_errors,
        store_errors,
        status

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        run_id,
        execution_time,
        rows_extracted,
        rows_passed,
        rows_failed,
        date_errors,
        amount_errors,
        store_errors,
        status

    ))

    conn.commit()

    conn.close()

    logger.info(f"Audit record inserted")