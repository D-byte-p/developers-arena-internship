import pandas as pd

# Load data
data = pd.read_csv("data/sales_data.csv")

# Show first rows
print("First 5 rows:")
print(data.head())

# Basic info
print("\nData Info:")
print(data.info())

# Total sales calculation
data["Total_Sales"] = data["Quantity"] * data["Price"]
print("\nTotal Sales:", data["Total_Sales"].sum())
