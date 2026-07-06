import pandas as pd
import mysql.connector

# -----------------------------
# Read cleaned CSV
# -----------------------------
df = pd.read_csv("data/processed/superstore_cleaned.csv")

# Clean column names
df.columns = (
    df.columns
      .str.strip()
      .str.replace(".", "_", regex=False)
      .str.replace(" ", "_", regex=False)
)



# Convert dates
df["Order_Date"] = pd.to_datetime(df["Order_Date"]).dt.date
df["Ship_Date"] = pd.to_datetime(df["Ship_Date"]).dt.date

# -----------------------------
# Connect MySQL
# -----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="retail_sales"
)

cursor = conn.cursor()

cursor.execute("DELETE FROM sales")

sql = """
INSERT INTO sales(
Row_ID,
Order_ID,
Order_Date,
Ship_Date,
Ship_Mode,
Customer_ID,
Customer_Name,
Segment,
City,
State,
Country,
Market,
Region,
Product_ID,
Category,
Sub_Category,
Product_Name,
Sales,
Quantity,
Discount,
Profit,
Shipping_Cost,
Order_Priority,
Year,
Market2,
WeekNum
)
VALUES(
%s,%s,%s,%s,%s,
%s,%s,%s,%s,%s,
%s,%s,%s,%s,%s,
%s,%s,%s,%s,%s,
%s,%s,%s,%s,%s,%s
)
"""

for _, row in df.iterrows():

    # Find the week column automatically
    

    values = (
        int(row["Row_ID"]),
        row["Order_ID"],
        row["Order_Date"],
        row["Ship_Date"],
        row["Ship_Mode"],
        row["Customer_ID"],
        row["Customer_Name"],
        row["Segment"],
        row["City"],
        row["State"],
        row["Country"],
        row["Market"],
        row["Region"],
        row["Product_ID"],
        row["Category"],
        row["Sub_Category"],
        row["Product_Name"],
        float(row["Sales"]),
        int(row["Quantity"]),
        float(row["Discount"]),
        float(row["Profit"]),
        float(row["Shipping_Cost"]),
        row["Order_Priority"],
        int(row["Year"]),
        row["Market2"],
        int(row["weeknum"])
    )

    cursor.execute(sql, values)

conn.commit()

print(f"Loaded {len(df)} rows successfully!")

cursor.close()
conn.close()

print("Data loaded into MySQL successfully!")