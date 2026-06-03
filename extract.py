import pandas as pd
from logger import logger

def extract_data(filepath):

    logger.info(f"Reading file: {filepath}")

    df = pd.read_csv(filepath)

    logger.info(f"Rows extracted: {len(df)}")

    return df