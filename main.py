import pandas as pd 
import matplotlib.pyplot as plt

try:
    df = pd.read_csv("sales_data.csv")
    print("Data Set Loaded Successfully!")
except FileNotFoundError:
    print("Error: sales_data.csv not found")
    exit()


df['Date'] = pd.to_datetime(df['Date'])

print("\nDataset Info: ")
print(df.info())


# Data Analysis
total_revenue = df['Total_Sales'].sum()

product_sales = df.groupby('Product')['Total_Sales'].sum()

region_sales = df.groupby('Region')['Total_Sales'].sum()

df['Month'] = df['Date'].dt.month
monthly_sales = df.groupby('Month')['Total_Sales'].sum()



print("\nTotal Revenue:",total_revenue)
print("\nSales by Product:\n",product_sales)
print("\nSales by Region:\n",region_sales)
print("\nMonthly Sales:\n",monthly_sales)


#Bar Chart
product_sales.plot(kind='bar')
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()

#Line Chart
plt.figure()
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

#pie Chart
region_sales.plot(kind='pie', autopct = '%1.1f%%')
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.tight_layout()
plt.savefig("region_sales.png")
plt.show()

print("\nAnalysis and Visualization completed successfully!")
