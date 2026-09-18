# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("data/ecommerce_sales.csv")

# Data Cleaning
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
df["Year"] = df["Order_Date"].dt.year

# Dataset Overview
print("\n===== DATASET OVERVIEW =====")
print(f"Total Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}")
print(f"Duplicate Rows: {df.duplicated().sum()}")
print("\nMissing Values:")
print(df.isnull().sum())

# Basic Business Metrics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
total_customers = df["Customer_ID"].nunique()
average_order_value = total_sales / total_orders

print("\n===== BASIC BUSINESS METRICS =====")
print(f"Total Sales: {total_sales:,.2f}")
print(f"Total Profit: {total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")
print(f"Average Order Value: {average_order_value:,.2f}")

# Category-wise Sales and Profit
category_summary = (
    df.groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\n===== CATEGORY ANALYSIS =====")
print(category_summary.round(2))

# Region-wise Sales and Profit
region_summary = (
    df.groupby("Region")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\n===== REGION ANALYSIS =====")
print(region_summary.round(2))

# Monthly Sales Analysis
monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
    .sort_index()
)

print("\n===== MONTHLY SALES =====")
print(monthly_sales.round(2))

# Top 10 Products
top_products = (
    df.groupby("Product_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== TOP 10 PRODUCTS =====")
print(top_products.round(2))

# Top 10 Customers
top_customers = (
    df.groupby("Customer_ID")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== TOP 10 CUSTOMERS =====")
print(top_customers.round(2))

# Repeat Customer Analysis
customer_orders = (
    df.groupby("Customer_ID")["Order_ID"]
    .nunique()
)

repeat_customers = customer_orders[customer_orders > 1]
repeat_customer_percentage = (
    repeat_customers.count() / customer_orders.count()
) * 100

print("\n===== CUSTOMER ANALYSIS =====")
print(f"Total Customers: {customer_orders.count()}")
print(f"Repeat Customers: {repeat_customers.count()}")
print(f"Repeat Customer Percentage: {repeat_customer_percentage:.2f}%")

# Payment Mode Analysis
payment_summary = (
    df.groupby("Payment_Mode")
    .agg(
        Total_Orders=("Order_ID", "nunique"),
        Total_Sales=("Sales", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\n===== PAYMENT MODE ANALYSIS =====")
print(payment_summary.round(2))

# Monthly Sales Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(
    x=monthly_sales.index,
    y=monthly_sales.values,
    marker="o"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    "visualizations/python_monthly_sales.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Category Sales Visualization
category_sales = category_summary["Total_Sales"]

plt.figure(figsize=(10, 6))
sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(
    "visualizations/python_category_sales.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Region Sales Visualization
region_sales = region_summary["Total_Sales"]

plt.figure(figsize=(8, 5))
sns.barplot(
    x=region_sales.index,
    y=region_sales.values
)
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(
    "visualizations/python_region_sales.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Top 10 Products Visualization
plt.figure(figsize=(10, 6))
sns.barplot(
    x=top_products.values,
    y=top_products.index
)
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(
    "visualizations/python_top_products.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Payment Mode Visualization
payment_orders = df["Payment_Mode"].value_counts()

plt.figure(figsize=(8, 5))
sns.barplot(
    x=payment_orders.index,
    y=payment_orders.values
)
plt.title("Orders by Payment Mode")
plt.xlabel("Payment Mode")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig(
    "visualizations/python_payment_mode.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Sales vs Profit Visualization
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    hue="Category"
)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(
    "visualizations/python_sales_vs_profit.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Correlation Heatmap
numeric_columns = [
    "Quantity",
    "Unit_Price",
    "Discount",
    "Sales",
    "Profit",
    "Profit_Margin"
]

correlation = df[numeric_columns].corr()

plt.figure(figsize=(10, 7))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(
    "visualizations/python_correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Final Analysis Summary
best_category = category_sales.idxmax()
best_region = region_sales.idxmax()
best_product = top_products.idxmax()
best_month = monthly_sales.idxmax()

print("\n===== FINAL ANALYSIS SUMMARY =====")
print(f"Highest Sales Category: {best_category}")
print(f"Highest Sales Region: {best_region}")
print(f"Top Selling Product: {best_product}")
print(f"Highest Sales Month: {best_month}")
print("\n===== ANALYSIS COMPLETED SUCCESSFULLY =====")