
import argparse
import os
import pandas as pd
import sqlite3
import logging
import yaml

# 設定 logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def load_config(config_path):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def validate_schema(df, expected_schema):
    for col, dtype in expected_schema.items():
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
        if dtype == "int" and not pd.api.types.is_integer_dtype(df[col]):
            raise TypeError(f"Column {col} is not int type")
        if dtype == "str" and not pd.api.types.is_string_dtype(df[col]):
            raise TypeError(f"Column {col} is not string type")
    return True

def ingest_to_sqlite(df, table_name, db_path="ingestion/output.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Path to config.yml")
    parser.add_argument("--table", required=True, help="Table name to ingest")
    parser.add_argument("--dry-run", action="store_true", help="Only validate, don't ingest")
    args = parser.parse_args()

    config = load_config(args.config)
    table_config = config.get(args.table)

    if not table_config:
        raise ValueError(f"No config found for table {args.table}")

    path = table_config["path"]
    expected_schema = table_config["schema"]

    logging.info(f"Loading Excel file from: {path}")
    df = pd.read_excel(path)

    logging.info("Validating schema...")
    validate_schema(df, expected_schema)

    if args.dry_run:
        logging.info("Dry run mode: schema valid ✅")
    else:
        logging.info("Ingesting to SQLite...")
        ingest_to_sqlite(df, args.table)
        logging.info(f"✅ Ingestion complete for table: {args.table}")

if __name__ == "__main__":
    main()
