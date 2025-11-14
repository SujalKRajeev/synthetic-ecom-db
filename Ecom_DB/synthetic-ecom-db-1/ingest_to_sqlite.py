# ingest_to_sqlite.py
# Overwrite existing tables in ecommerce.db with CSV contents.
# Usage: python ingest_to_sqlite.py

import sqlite3
import pandas as pd
import os
import shutil

DB_NAME = "ecommerce.db"
DATA_DIR = "data"

# --- Optional: keep a timestamped backup of the old DB if it exists ---
if os.path.exists(DB_NAME):
    backup_name = f"{DB_NAME}.bak"
    # If you want a timestamped backup, uncomment below and comment the line above
    # import datetime
    # backup_name = f"{DB_NAME}.bak_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copyfile(DB_NAME, backup_name)
    print(f"Existing DB backed up as: {backup_name}")

# Connect to (or create) the database
conn = sqlite3.connect(DB_NAME)

# Files mapping (must match filenames in data/)
files = {
    "customers": "customers.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "reviews": "reviews.csv"
}

# Read CSVs and replace tables (if_exists='replace')
for table, fname in files.items():
    path = os.path.join(DATA_DIR, fname)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Required file not found: {path}")
    df = pd.read_csv(path)
    # Replace the table with fresh data (drops old table and creates new one)
    df.to_sql(table, conn, if_exists='replace', index=False)
    print(f"Replaced table '{table}' with {len(df)} rows from {fname}")

conn.close()
print("Done — all tables replaced in", DB_NAME)
