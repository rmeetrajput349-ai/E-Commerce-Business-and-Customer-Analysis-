use ecommerce_db;
SELECT 
    Customer_ID,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM ecommerce_sales
GROUP BY Customer_ID
ORDER BY Total_Sales DESC
LIMIT 10;