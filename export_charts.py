import sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# connect to the DB created by setup_sqlite.py
con = sqlite3.connect("sales.db")

# read aggregates with SQL
monthly = pd.read_sql(
    """
    SELECT strftime('%Y-%m', date) AS month,
           SUM(quantity*unit_price) AS revenue
    FROM sales
    GROUP BY month
    ORDER BY month
    """,
    con,
)

top_prod = pd.read_sql(
    """
    SELECT product,
           SUM(quantity*unit_price) AS revenue
    FROM sales
    GROUP BY product
    ORDER BY revenue DESC
    """,
    con,
)

# make charts
Path("charts").mkdir(exist_ok=True)

plt.figure()
monthly.plot(x="month", y="revenue")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("charts/monthly_revenue.png", dpi=150)

plt.figure()
top_prod.plot(kind="bar", x="product", y="revenue")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("charts/revenue_by_product.png", dpi=150)

print("Saved charts in charts/: monthly_revenue.png, revenue_by_product.png")
