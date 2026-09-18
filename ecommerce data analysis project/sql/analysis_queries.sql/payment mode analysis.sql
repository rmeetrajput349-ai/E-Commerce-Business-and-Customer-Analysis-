use ecommerce_db;
SELECT 
    Payment_Mode,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM ecommerce_sales
GROUP BY Payment_Mode
ORDER BY Total_Sales DESC;