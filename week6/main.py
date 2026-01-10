import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/sales_data.csv")

# Create visualization folder
import os
os.makedirs("visualizations", exist_ok=True)

# 1. Bar Chart
plt.figure()
sns.barplot(x="Category", y="Price", data=df)
plt.title("Average Price by Category")
plt.savefig("visualizations/bar_chart.png")
plt.close()

# 2. Line Chart
plt.figure()
sns.lineplot(x=df.index, y="Price", data=df)
plt.title("Price Trend")
plt.savefig("visualizations/line_chart.png")
plt.close()

# 3. Box Plot
plt.figure()
sns.boxplot(x="Category", y="Price", data=df)
plt.title("Price Distribution by Category")
plt.savefig("visualizations/box_plot.png")
plt.close()

# 4. Heatmap
plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("visualizations/heatmap.png")
plt.close()

# 5. Pie Chart
plt.figure()
df["Category"].value_counts().plot.pie(autopct="%1.1f%%")
plt.title("Category Distribution")
plt.savefig("visualizations/pie_chart.png")
plt.close()

print("All visualizations created successfully!")
