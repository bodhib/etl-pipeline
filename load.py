import sqlite3
from logger import logger

from config import config

import sys

DATABASE = config["database"]

import sqlite3

def load_data(df):
    # print(df)
    # sys.exit(0)
    logger.info("Loading data into database")

    try:
        with sqlite3.connect(DATABASE, timeout=10) as conn:
            df.to_sql(
                "sales",
                conn,
                if_exists="append",
                index=False
            )
            conn.commit()
        logger.info("Data loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load data: {e}")