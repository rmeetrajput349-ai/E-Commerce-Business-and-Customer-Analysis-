use ecommerce_db;
SELECT 
    ROUND(SUM(Sales) / COUNT(DISTINCT Order_ID), 2) AS Average_Order_Value
FROM ecommerce_sales;