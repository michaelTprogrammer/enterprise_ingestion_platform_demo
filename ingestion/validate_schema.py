
import pandas as pd
import yaml
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

def load_schema(config_path, table_name):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config['tables'][table_name]['columns']

def validate_schema(file_path, schema_def):
    df = pd.read_excel(file_path) if file_path.endswith('.xlsx') else pd.read_csv(file_path)
    expected_cols = [col['name'] for col in schema_def]
    actual_cols = df.columns.tolist()

    if expected_cols != actual_cols:
        raise ValueError(f"Schema mismatch!\nExpected: {expected_cols}\nActual: {actual_cols}")
    logging.info("✅ Schema validated successfully.")
    return True

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True, help='Path to config.yml')
    parser.add_argument('--table', required=True, help='Table name in config')
    args = parser.parse_args()

    config_path = args.config
    table_name = args.table
    file_path = os.path.join('data', f"{table_name}.xlsx")

    schema_def = load_schema(config_path, table_name)
    validate_schema(file_path, schema_def)
