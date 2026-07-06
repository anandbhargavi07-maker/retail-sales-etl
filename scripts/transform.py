import pandas as pd


def transform_data(df):
    """
    Clean and transform the dataset.
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove leading/trailing spaces from column names
    df.columns = df.columns.str.strip()

    # Convert dates
    df["Order.Date"] = pd.to_datetime(df["Order.Date"])
    df["Ship.Date"] = pd.to_datetime(df["Ship.Date"])

    # Create new features
    df["Order_Year"] = df["Order.Date"].dt.year
    df["Order_Month"] = df["Order.Date"].dt.month_name()
    df["Order_Quarter"] = df["Order.Date"].dt.quarter
    df["Order_Weekday"] = df["Order.Date"].dt.day_name()

    # Profit Margin
    df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100

    # Delivery Days
    df["Delivery_Days"] = (
        df["Ship.Date"] - df["Order.Date"]
    ).dt.days

    return df


if __name__ == "__main__":

    df = pd.read_csv(
        "data/raw/superstore.csv",
        encoding="latin1"
    )

    transformed_df = transform_data(df)
    
    import os

os.makedirs("data/processed", exist_ok=True)

transformed_df.to_csv(
    "data/processed/superstore_cleaned.csv",
    index=False
)

print("Cleaned dataset saved successfully!")

print("Transformation Complete!")