-- Monthly revenue
SELECT strftime('%Y-%m', date) AS month, 
       ROUND(SUM(quantity*unit_price),2) AS total_revenue
FROM sales 
GROUP BY month 
ORDER BY month;

-- Top products
SELECT product, 
       ROUND(SUM(quantity*unit_price),2) AS revenue
FROM sales 
GROUP BY product 
ORDER BY revenue DESC;

-- Region share
SELECT region, 
       ROUND(SUM(quantity*unit_price),2) AS revenue
FROM sales 
GROUP BY region 
ORDER BY revenue DESC;

-- Channel AOV
SELECT channel, 
       ROUND(AVG(quantity*unit_price),2) AS avg_order_value
FROM sales 
GROUP BY channel;
