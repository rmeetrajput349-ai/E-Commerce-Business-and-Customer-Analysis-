use ecommerce_db;
SELECT Region, ROUND(SUM(Sales), 2) AS Total_Sales FROM ecommerce_sales
GROUP BY Region
ORDER BY Total_Sales DESC;