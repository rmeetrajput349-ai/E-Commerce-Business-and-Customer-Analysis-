use ecommerce_db;
SELECT 
    Region,
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM ecommerce_sales
GROUP BY Region, Category
ORDER BY Region, Total_Sales DESC;