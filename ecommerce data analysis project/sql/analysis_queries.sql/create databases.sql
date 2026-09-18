use ecommerce_db;
CREATE TABLE ecommerce_sales (
    Order_ID VARCHAR(20) PRIMARY KEY,
    Order_Date DATE,
    Customer_ID VARCHAR(20),
    Product_ID VARCHAR(20),
    Product_Name VARCHAR(100),
    Category VARCHAR(50),
    Quantity INT,
    Unit_Price DECIMAL(10,2),
    Discount DECIMAL(5,2),
    Sales DECIMAL(12,2),
    Profit DECIMAL(12,2),
    Region VARCHAR(30),
    Payment_Mode VARCHAR(30)
);