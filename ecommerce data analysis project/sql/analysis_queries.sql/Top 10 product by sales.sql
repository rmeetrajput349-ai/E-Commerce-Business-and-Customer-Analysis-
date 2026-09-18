use ecommerce_db;
SELECT Product_Name, ROUND(SUM(Sales), 2) AS Total_Sales FROM ecommerce_sales
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;