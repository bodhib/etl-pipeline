import sqlite3
from logger import logger

from config import config

DATABASE = config["database"]

def fetch_data():
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sales")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()

    logger.info("Data fetched successfully to verify ETL pipeline completion")