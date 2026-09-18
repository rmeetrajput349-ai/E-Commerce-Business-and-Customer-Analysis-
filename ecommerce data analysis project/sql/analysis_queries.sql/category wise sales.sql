use ecommerce_db;
SELECT Category, ROUND(SUM(Sales), 2) AS Total_Sales FROM ecommerce_sales
GROUP BY Category
ORDER BY Total_Sales DESC;