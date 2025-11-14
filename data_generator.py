# data_generator.py
# Generates synthetic e-commerce CSV files:
# customers.csv, products.csv, orders.csv, order_items.csv, reviews.csv
# Usage: pip install faker pandas
#        python data_generator.py

import os
import random
from datetime import datetime, timedelta
import pandas as pd
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

OUT_DIR = "data"
os.makedirs(OUT_DIR, exist_ok=True)

N_CUSTOMERS = 800
N_PRODUCTS = 200
N_ORDERS = 1200
MAX_ITEMS_PER_ORDER = 6
N_REVIEWS = 900

# 1) customers.csv
customers = []
for cid in range(1, N_CUSTOMERS + 1):
    name = fake.name()
    email = fake.unique.safe_email()
    signup_date = fake.date_between(start_date="-3y", end_date="today")
    customers.append({
        "customer_id": cid,
        "name": name,
        "email": email,
        "signup_date": signup_date
    })
df_customers = pd.DataFrame(customers)
df_customers.to_csv(os.path.join(OUT_DIR, "customers.csv"), index=False)
print(f"Written {len(df_customers)} customers")

# 2) products.csv
categories = ["Electronics", "Clothing", "Home", "Toys", "Sports", "Books", "Beauty"]
products = []
for pid in range(1, N_PRODUCTS + 1):
    pname = fake.word().capitalize() + " " + fake.word().capitalize()
    category = random.choice(categories)
    # price between 5 and 1000, with two decimals
    price = round(random.uniform(5, 1000), 2)
    products.append({
        "product_id": pid,
        "name": pname,
        "category": category,
        "price": price
    })
df_products = pd.DataFrame(products)
df_products.to_csv(os.path.join(OUT_DIR, "products.csv"), index=False)
print(f"Written {len(df_products)} products")

# 3) orders.csv and 4) order_items.csv
orders = []
order_items = []
order_id_seq = 1
order_item_seq = 1

for oid in range(1, N_ORDERS + 1):
    customer_id = random.randint(1, N_CUSTOMERS)
    # order within last 2 years
    order_date = fake.date_between(start_date="-2y", end_date="today")
    n_items = random.randint(1, MAX_ITEMS_PER_ORDER)
    items_in_order = []
    total_amount = 0.0

    for _ in range(n_items):
        product_id = random.randint(1, N_PRODUCTS)
        quantity = random.randint(1, 5)
        product_price = df_products.loc[df_products['product_id'] == product_id, 'price'].values[0]
        line_total = round(product_price * quantity, 2)

        order_items.append({
            "order_item_id": order_item_seq,
            "order_id": oid,
            "product_id": product_id,
            "quantity": quantity
        })
        order_item_seq += 1
        total_amount += line_total

    total_amount = round(total_amount, 2)
    orders.append({
        "order_id": oid,
        "customer_id": customer_id,
        "order_date": order_date,
        "total_amount": total_amount
    })

df_orders = pd.DataFrame(orders)
df_order_items = pd.DataFrame(order_items)

df_orders.to_csv(os.path.join(OUT_DIR, "orders.csv"), index=False)
df_order_items.to_csv(os.path.join(OUT_DIR, "order_items.csv"), index=False)
print(f"Written {len(df_orders)} orders and {len(df_order_items)} order_items")

# 5) reviews.csv
reviews = []
for rid in range(1, N_REVIEWS + 1):
    customer_id = random.randint(1, N_CUSTOMERS)
    product_id = random.randint(1, N_PRODUCTS)
    rating = random.randint(1, 5)
    review_text = fake.sentence(nb_words=12)
    reviews.append({
        "review_id": rid,
        "customer_id": customer_id,
        "product_id": product_id,
        "rating": rating,
        "review_text": review_text
    })
df_reviews = pd.DataFrame(reviews)
df_reviews.to_csv(os.path.join(OUT_DIR, "reviews.csv"), index=False)
print(f"Written {len(df_reviews)} reviews")

print("All files generated in the 'data/' directory.")
