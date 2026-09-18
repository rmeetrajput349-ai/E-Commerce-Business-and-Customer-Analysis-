use ecommerce_db;
SELECT
    Order_ID,
    Sales,
    CASE
        WHEN Sales < 5000 THEN 'Low Value'
        WHEN Sales BETWEEN 5000 AND 20000 THEN 'Medium Value'
        ELSE 'High Value'
    END AS Order_Category
FROM ecommerce_sales
ORDER BY Sales DESC;