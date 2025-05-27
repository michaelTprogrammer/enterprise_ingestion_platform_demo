
#!/bin/bash

# Shell script to run full ingestion flow

TABLE=$1
CONFIG_PATH="ingestion/config.yml"
FILE_PATH="data/${TABLE}.xlsx"

echo "🚀 Running ingestion for table: $TABLE"

echo "🔍 Step 1: Validating schema..."
python ingestion/validate_schema.py --config $CONFIG_PATH --table $TABLE

echo "📥 Step 2: Loading into warehouse..."
python ingestion/load_to_warehouse.py --file $FILE_PATH --table $TABLE

echo "✅ Ingestion complete."
