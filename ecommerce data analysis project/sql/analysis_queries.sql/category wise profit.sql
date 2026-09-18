use ecommerce_db;
SELECT Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM ecommerce_sales
GROUP BY Category
ORDER BY Total_Profit DESC;