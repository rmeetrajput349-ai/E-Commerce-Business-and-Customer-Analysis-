use ecommerce_db;
SELECT 
    Customer_ID,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM ecommerce_sales
GROUP BY Customer_ID
HAVING COUNT(DISTINCT Order_ID) > 1
ORDER BY Total_Orders DESC;