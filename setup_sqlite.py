import sqlite3, pandas as pd
from pathlib import Path

db = Path("sales.db")
csv = Path("data") / "sales.csv"

con = sqlite3.connect(db)
df = pd.read_csv(csv, parse_dates=["date"])
df.to_sql("sales", con, if_exists="replace", index=False)

with con:
    con.execute("CREATE INDEX IF NOT EXISTS idx_date ON sales(date)")
    con.execute("CREATE INDEX IF NOT EXISTS idx_region ON sales(region)")

print("Loaded data into sales.db (table: sales)")
