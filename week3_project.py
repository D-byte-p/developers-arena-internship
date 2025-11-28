import pandas as pd

# Week 3 Project: Sales Data Analysis

# 1. Read the CSV file
df = pd.read_csv("sales_data.csv")

print("First 5 rows of the dataset:")
print(df.head())
print("\nBasic info about dataset:")
print(df.info())

# 2. Check for missing values (data cleaning basic step)
print("\nMissing values in each column:")
print(df.isnull().sum())

# 3. Create a 'Total' column = Quantity * Price
df["Total"] = df["Quantity"] * df["Price"]

print("\nDataset with Total column:")
print(df.head())

# 4. Find total sales
total_sales = df["Total"].sum()

# 5. Find best-selling product (by total sales amount)
sales_by_product = df.groupby("Product")["Total"].sum()
best_product = sales_by_product.idxmax()
best_product_sales = sales_by_product.max()

# 6. Some extra simple stats
max_sale = df["Total"].max()
min_sale = df["Total"].min()
average_sale = df["Total"].mean()

# 7. Final report
print("\n--- Sales Report ---")
print(f"Total sales (all products): ₹{total_sales}")
print("\nSales by product:")
print(sales_by_product)

print(f"\nBest-selling product: {best_product} (₹{best_product_sales})")
print(f"Highest single sale amount: ₹{max_sale}")
print(f"Lowest single sale amount: ₹{min_sale}")
print(f"Average sale amount: ₹{average_sale:.2f}")

print("\nGreat job! You just analyzed a real sales dataset using Pandas 🐼")
