import pandas as pd

def extract_data(file_path):
    """
    Extract data from CSV file.
    """
    df = pd.read_csv(file_path, encoding="latin1")
    return df


if __name__ == "__main__":
    file_path = "data/raw/superstore.csv"

    df = extract_data(file_path)

    print("Data extracted successfully!")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")