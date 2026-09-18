use ecommerce_db;
SELECT
    CASE
        WHEN Sales < 5000 THEN 'Low Value'
        WHEN Sales BETWEEN 5000 AND 20000 THEN 'Medium Value'
        ELSE 'High Value'
    END AS Order_Category,
    COUNT(*) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM ecommerce_sales
GROUP BY Order_Category
ORDER BY Total_Sales DESC;