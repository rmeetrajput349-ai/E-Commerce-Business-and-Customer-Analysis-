use ecommerce_db;
SELECT 
    ROUND(
        (SUM(Profit) / SUM(Sales)) * 100,
        2
    ) AS Profit_Margin_Percentage
FROM ecommerce_sales;