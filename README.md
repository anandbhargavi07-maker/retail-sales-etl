# Retail Sales ETL Pipeline

## Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using the Global Superstore dataset.

The pipeline extracts raw sales data, performs data cleaning and feature engineering with Pandas, loads the transformed data into MySQL, and visualizes key business insights using Power BI.

---

## Tech Stack

- Python
- Pandas
- MySQL
- Power BI
- VS Code

---

## Project Structure

```
retail-sales-etl/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│
├── sql/
│   └── create_tables.sql
│
├── dashboard/
│   └── Retail_Sales_Dashboard.pbix
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ETL Workflow

```
Raw CSV
      │
      ▼
Extract (Python)
      │
      ▼
Transform (Pandas)
      │
      ▼
Load (MySQL)
      │
      ▼
Power BI Dashboard
```

---

## Dashboard KPIs

- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Sales by Category
- Sales by Region
- Monthly Sales Trend
- Top 10 Products
- Profit by Segment

---

## Dataset

Global Superstore Dataset

---

## Author

Bhargavi Anand