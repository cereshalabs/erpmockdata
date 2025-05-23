# erpmockdata – Simulated ERP Data Generator for Prototyping

**Version 1.0**

This tool helps consultants and data engineers quickly prototype manufacturing ERP pipelines without relying on real customer data.

It can generate realistic data tables that are common in a production ERP system — such as product specs, assembly stations, operators, and order history — using Python and the Faker library.

---

## 📌 Why This Exists

As a data engineering consultant, I often need to build out pipeline demos, test ETL frameworks, or validate transformations — **before any production access is granted**.

Rather than waiting on customer data or mocking it manually, this tool generates clean, referentially consistent datasets in seconds.

---

## 📁 Project Structure

```
fake-erp-data/
├── data/ # Generated CSVs (output)
├── notebooks/ # (Optional) Jupyter notebooks for exploration
├── src/ # Python scripts and generators
│ └── generate_data.py
├── requirements.txt
```

## Generate Sample Data

Run the generator script

python src/generate_data.py

This will create 4 CSV files in the `data/` directory:

- `products.csv`
- `stations.csv`
- `operators.csv`
- `orders.csv`


