
import pandas as pd
import sqlite3
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

def load_data_to_sqlite(file_path, table_name, db_path='data/output.db'):
    try:
        logging.info(f"📦 Loading file: {file_path} into table: {table_name}")
        df = pd.read_excel(file_path) if file_path.endswith('.xlsx') else pd.read_csv(file_path)

        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()

        logging.info(f"✅ Successfully loaded data into table '{table_name}' in {db_path}")
    except Exception as e:
        logging.error(f"❌ Error loading data: {e}")
        raise

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help='Path to input file')
    parser.add_argument('--table', required=True, help='Target table name')
    parser.add_argument('--db', default='data/output.db', help='Path to SQLite DB')
    args = parser.parse_args()

    load_data_to_sqlite(args.file, args.table, args.db)
