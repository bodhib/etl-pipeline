import pandas as pd
from logger import logger

import sys

def transform_data(df):
    # print(df)
    # sys.exit(0)
    logger.info("Starting transformation")

    # Remove duplicates, keeping the first occurrence
    df = df.drop_duplicates(subset=["store_id", "sales_date"])

    # Add derived columns
    df["tax"] = df["amount"] * 0.18
    df["net_amount"] = df["amount"] - df["tax"]

    logger.info(f"Valid rows after transformation: {len(df)}")
    return df