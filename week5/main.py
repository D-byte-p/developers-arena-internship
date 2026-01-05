import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
data = pd.read_csv("data/sales_data.csv")

print("First 5 rows:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())

# Create Total Sales column
data["Total_Sales"] = data["Quantity"] * data["Price"]

# Total revenue
total_revenue = data["Total_Sales"].sum()
print("\nTotal Revenue:", total_revenue)

# Sales by Product
product_sales = data.groupby("Product")["Total_Sales"].sum()
print("\nSales by Product:")
print(product_sales)

# Sales by Month
data["Month"] = pd.to_datetime(data["Date"]).dt.month
monthly_sales = data.groupby("Month")["Total_Sales"].sum()
print("\nMonthly Sales:")
print(monthly_sales)

# Create visualization folder if not exists
os.makedirs("visualization", exist_ok=True)

# Bar Chart – Sales by Product
plt.figure()
product_sales.plot(kind="bar", title="Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualization/bar_chart.png")
plt.close()

# Line Chart – Monthly Sales
plt.figure()
monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualization/line_chart.png")
plt.close()

print("\nCharts saved successfully in visualization folder.")
