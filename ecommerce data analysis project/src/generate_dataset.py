import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

categories = ["Electronics", "Furniture", "Clothing", "Books", "Home & Kitchen"]
products = {
    "Electronics": ["Laptop", "Smartphone", "Headphones", "Keyboard", "Mouse"],
    "Furniture": ["Chair", "Table", "Bookshelf", "Sofa", "Desk"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket", "Shoes", "Hoodie"],
    "Books": ["Python Book", "SQL Book", "Data Science Book", "Novel", "Business Book"],
    "Home & Kitchen": ["Mixer", "Cookware Set", "Lamp", "Bottle", "Coffee Maker"]
}

regions = ["North", "South", "East", "West", "Central"]
payment_modes = ["Credit Card", "Debit Card", "UPI", "Cash on Delivery"]

category = np.random.choice(categories, n)
product = [np.random.choice(products[c]) for c in category]

unit_price = np.random.randint(300, 60000, n)
quantity = np.random.randint(1, 6, n)
discount = np.random.choice([0, 5, 10, 15, 20], n)

sales = unit_price * quantity * (1 - discount / 100)

profit_margin = np.random.uniform(0.08, 0.25, n)
profit = sales * profit_margin

df = pd.DataFrame({
    "Order_ID": [f"ORD{i:04d}" for i in range(1, n + 1)],
    "Order_Date": pd.date_range("2024-01-01", "2024-12-31", periods=n),
    "Customer_ID": [f"CUST{np.random.randint(1, 301):04d}" for _ in range(n)],
    "Product_ID": [f"PROD{np.random.randint(1, 101):04d}" for _ in range(n)],
    "Product_Name": product,
    "Category": category,
    "Quantity": quantity,
    "Unit_Price": unit_price,
    "Discount": discount,
    "Sales": sales.round(2),
    "Profit": profit.round(2),
    "Region": np.random.choice(regions, n),
    "Payment_Mode": np.random.choice(payment_modes, n)
})

df.to_csv("data/ecommerce_sales.csv", index=False)

print("Dataset created successfully!")
print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")