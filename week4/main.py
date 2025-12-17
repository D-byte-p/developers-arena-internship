# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load dataset
data = pd.read_csv("data/sales_data.csv")

# Step 3: View first 5 rows
print("First 5 rows of the dataset:")
print(data.head())

# Step 4: Basic information about data
print("\nDataset Information:")
data.info()   # info() ko print ke andar nahi rakhte

# Step 5: Statistical summary
print("\nStatistical Summary:")
print(data.describe())

# Step 6: Check column names
print("\nColumn names:")
print(list(data.columns))

# Step 7: Check missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Step 8: Data types
print("\nData types of each column:")
print(data.dtypes)

# Step 9: Check duplicate rows
print("\nDuplicate rows:", data.duplicated().sum())


# =========================
# SAFE SALES COLUMN HANDLING
# =========================

# Automatically find sales column
sales_column = None
for col in data.columns:
    if col.lower() in ["sales", "revenue", "amount", "sales_amount"]:
        sales_column = col
        break

if sales_column is None:
    print("\n❌ No Sales column found. Check dataset column names.")
else:
    print(f"\n✅ Sales column detected: {sales_column}")

    # Step 10: Total sales
    total_sales = data[sales_column].sum()
    print("\nTotal Sales:", total_sales)

    # Step 11: Sales by Category (only if Category exists)
    if "Category" in data.columns:
        category_sales = data.groupby("Category")[sales_column].sum()
        print("\nSales by Category:")
        print(category_sales)
    else:
        print("\n⚠️ Category column not found")

    # Step 12: Sales by Month (only if Month exists)
    if "Month" in data.columns:
        monthly_sales = data.groupby("Month")[sales_column].sum()
        print("\nSales by Month:")
        print(monthly_sales)
    else:
        print("\n⚠️ Month column not found")

# Step 13: Unique products (optional)
if "Product" in data.columns:
    print("\nUnique products:")
    print(data["Product"].unique())
# =========================
# VISUALIZATION 1: BAR CHART
# =========================

if "Product" in data.columns and "Total_Sales" in data.columns:
    product_sales = data.groupby("Product")["Total_Sales"].sum()

    plt.figure(figsize=(8, 5))
    plt.bar(product_sales.index, product_sales.values)
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("visualizations/bar_chart.png")
    plt.show()
else:
    print("⚠ Cannot create bar chart (Product or Total_Sales column missing)")
# =========================
# VISUALIZATION 2: LINE CHART
# =========================

if "Date" in data.columns and "Total_Sales" in data.columns:
    # Convert Date column to datetime
    data["Date"] = pd.to_datetime(data["Date"])

    # Group by Date
    daily_sales = data.groupby("Date")["Total_Sales"].sum()

    plt.figure(figsize=(10, 5))
    plt.plot(daily_sales.index, daily_sales.values, marker='o')
    plt.title("Total Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("visualizations/line_chart.png")
    plt.show()
else:
    print("⚠ Cannot create line chart (Date or Total_Sales column missing)")

