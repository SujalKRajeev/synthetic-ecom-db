import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")

query = """
SELECT
    c.name AS customer_name,
    c.email AS customer_email,
    p.name AS product_name,
    p.category AS product_category,
    o.order_date,
    oi.quantity,
    o.total_amount
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON p.product_id = oi.product_id
ORDER BY o.order_date DESC
LIMIT 20;
"""

df = pd.read_sql_query(query, conn)
print(df)

conn.close()
