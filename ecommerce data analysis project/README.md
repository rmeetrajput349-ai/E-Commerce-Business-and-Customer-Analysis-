# E-Commerce Sales Data Analysis

## 📌 Project Overview

This project is an end-to-end **E-Commerce Sales Data Analysis** project built using Python, SQL, and data visualization tools.

The project analyzes sales, profit, customers, products, regions, categories, and payment methods to identify meaningful business insights from e-commerce data.

---

## 🎯 Project Objectives

* Analyze overall sales and profit performance
* Identify top-performing product categories
* Analyze regional sales performance
* Identify monthly sales trends
* Find top-selling products
* Analyze customer purchasing behavior
* Identify repeat customers
* Analyze payment method preferences
* Study the relationship between sales and profit
* Generate meaningful business insights through visualization

---

## 🛠️ Technologies Used

| Technology       | Purpose                        |
| ---------------- | ------------------------------ |
| Python           | Data analysis and automation   |
| Pandas           | Data manipulation and analysis |
| NumPy            | Numerical operations           |
| Matplotlib       | Data visualization             |
| Seaborn          | Statistical visualization      |
| MySQL            | SQL-based business analysis    |
| Jupyter Notebook | Exploratory Data Analysis      |
| VS Code          | Python development             |

---

## 📂 Project Structure

```text
ecommerce-data-analysis-project/
│
├── 📁 data/
│   └── ecommerce_sales.csv
│
├── 📁 notebooks/
│   └── ecommerce_analysis.ipynb
│
├── 📁 sql/
│   └── analysis_queries.sql
│
├── 📁 src/
│   ├── generate_dataset.py
│   └── analysis.py
│
├── 📁 visualizations/
│   ├── monthly_sales.png
│   ├── category_sales.png
│   ├── region_sales.png
│   ├── top_products.png
│   ├── payment_mode.png
│   ├── sales_vs_profit.png
│   ├── correlation_heatmap.png
│   ├── python_monthly_sales.png
│   ├── python_category_sales.png
│   ├── python_region_sales.png
│   ├── python_top_products.png
│   ├── python_payment_mode.png
│   ├── python_sales_vs_profit.png
│   └── python_correlation_heatmap.png
│
└── 📄 README.md
```

---

## 📊 Dataset

The dataset contains **1,000 e-commerce sales records** covering orders, customers, products, categories, regions, pricing, discounts, sales, profit, and payment methods.

### Key Columns

* `Order_ID` — Unique order identifier
* `Order_Date` — Date of the order
* `Customer_ID` — Unique customer identifier
* `Product_Name` — Product purchased
* `Category` — Product category
* `Region` — Customer/order region
* `Quantity` — Quantity purchased
* `Unit_Price` — Price per unit
* `Discount` — Discount applied
* `Sales` — Total sales amount
* `Profit` — Profit generated
* `Payment_Mode` — Payment method used

---

## 🐍 Python Analysis

Python was used to perform the following analysis:

* Data loading and preprocessing
* Missing-value checking
* Duplicate-value checking
* Date conversion
* Feature engineering
* Sales and profit calculations
* Category-wise analysis
* Region-wise analysis
* Monthly sales analysis
* Product performance analysis
* Customer analysis
* Repeat customer analysis
* Payment mode analysis
* Correlation analysis

---

## 🗄️ SQL Analysis

MySQL was used for business-oriented data analysis.

The SQL analysis includes:

* Total sales calculation
* Total profit calculation
* Total order count
* Category-wise sales
* Category-wise profit
* Region-wise sales
* Region-wise profit
* Monthly sales analysis
* Top-selling products
* Customer analysis
* Payment mode analysis

All SQL queries are stored in:

```text
sql/analysis_queries.sql
```

---

## 📓 Jupyter Notebook

Jupyter Notebook was used for exploratory data analysis and step-by-step visualization.

The notebook includes:

* Dataset exploration
* Data cleaning
* Feature engineering
* Statistical analysis
* Category analysis
* Regional analysis
* Product analysis
* Customer analysis
* Monthly sales analysis
* Data visualization
* Correlation analysis
* Business insights

Notebook:

```text
notebooks/ecommerce_analysis.ipynb
```

---

## 📈 Data Visualizations

The project includes the following visualizations:

* 📈 Monthly Sales Trend
* 📊 Sales by Category
* 📊 Sales by Region
* 📊 Top 10 Products by Sales
* 📊 Orders by Payment Mode
* 🔵 Sales vs Profit
* 🔥 Correlation Heatmap

All visualization files are available in:

```text
visualizations/
```

---

## 💡 Key Business Insights

Based on the analysis:

* **Books** generated the highest total sales among the product categories.
* **Books** also generated the highest total profit.
* The **North region** recorded the highest total sales.
* **March 2024** recorded the highest monthly sales.
* **Mouse** was the highest-selling product by total sales.
* Customer-level analysis was used to identify high-value and repeat customers.
* Payment mode analysis was used to understand customer payment preferences.

---

## 🔄 Project Workflow

```text
              Raw E-Commerce Dataset
                       │
                       ▼
                Data Generation
                       │
                       ▼
                 Data Cleaning
                       │
              ┌────────┴────────┐
              ▼                 ▼
        MySQL Analysis     Python Analysis
              │                 │
              └────────┬────────┘
                       ▼
              Exploratory Analysis
                       │
                       ▼
                Data Visualization
                       │
                       ▼
                 Business Insights
```

---

## ▶️ How to Run the Project

### Run Python Analysis

Open the project in VS Code and run:

```bash
python src/analysis.py
```

The script performs the analysis and generates visualization files inside the `visualizations` folder.

### Run Jupyter Notebook

Open:

```text
notebooks/ecommerce_analysis.ipynb
```

Run the notebook cells to view the complete exploratory analysis and visualizations.

### Run SQL Analysis

Open **MySQL Workbench**, select the project database, and execute:

```text
sql/analysis_queries.sql
```

---

## 📌 Project Highlights

* 1,000 e-commerce records analyzed
* Python-based data analysis
* MySQL business analysis
* Exploratory Data Analysis using Jupyter Notebook
* Data visualization using Matplotlib and Seaborn
* Customer and product analysis
* Regional and category performance analysis
* Business insights generation

---

## 🏁 Conclusion

This project demonstrates a complete data analysis workflow by combining **Python, SQL, Jupyter Notebook, and data visualization**.

The analysis transforms raw e-commerce data into meaningful business insights related to sales performance, customer behavior, product performance, regional trends, and payment preferences.
