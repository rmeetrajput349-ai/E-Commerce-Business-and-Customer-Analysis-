use ecommerce_db;
SELECT DATE_FORMAT(Order_Date, '%Y-%m') AS Month, ROUND(SUM(Sales), 2) AS Total_Sales FROM ecommerce_sales
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY Month;