
# 📦 Synthetic E-Commerce Database (SQLite)

This project demonstrates how to use **Cursor IDE** to generate synthetic e-commerce data, ingest it into an **SQLite database**, and run **SQL queries** that join multiple tables.

This was completed as part of a **Cursor AI A-SDLC exercise**.

---

## 🚀 Project Tasks

### **1. Push Code Using GitHub**

The project is linked to a GitHub repository and all updates are pushed through Cursor IDE.

---

### **2. Generate Synthetic E-Commerce Data**

Using Cursor prompts, synthetic datasets were generated for typical e-commerce operations such as:

* Customers
* Products
* Orders
* Order Items
* Reviews

Data generation libraries like **pandas**, **faker**, and **random** were used.

---

### **3. Ingest Data Into SQLite**

A Python script ingests the generated CSV/JSON data into an **SQLite database** (`ecommerce.db`).

This includes:

* Creating tables
* Inserting records
* Validating data load

---

### **4. SQL Query on Multiple Tables**

A SQL query was written to **join multiple e-commerce tables** and produce a meaningful report—for example:

* Customer purchase history
* Product sales performance
* Order-level summaries

The query was generated and executed using Cursor IDE with SQLite.

---

## 🛠️ Technologies Used

* **Cursor AI IDE**
* **Python**

  * `pandas`
  * `faker`
  * `sqlite3`
* **SQLite3**
* **Git & GitHub**

---

## 📁 Folder Structure

```
synthetic-ecom-db/
│
├── data_generator.py
├── ingest_to_sqlite.py
├── run_query.py
├── ecommerce.db
└── README.md
```

---

## 📌 How to Run

### Install dependencies

```bash
pip install pandas faker
```

### Generate synthetic data

```bash
python data_generator.py
```

### Ingest into SQLite

```bash
python ingest_to_sqlite.py
```

### Run SQL join query

```bash
python run_query.py
```

---

## 📝 Notes

* Exercise performed and completed fully in **Cursor IDE**.
* Designed following the **A-SDLC workflow**.
* Demonstrates full pipeline: *Generate → Ingest → Query → Push to GitHub*.


✅ A **better version with screenshots**
✅ A **roadmap diagram**
✅ A **badges-style README** (like pro GitHub projects)
