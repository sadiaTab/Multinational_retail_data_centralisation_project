SELECT ROUND(SUM(o.product_quantity * p.product_price)::numeric,2) as total_sales,
d.year, d.month
FROM 
orders_table o
JOIN 
dim_products p ON o.product_code = p.product_code
JOIN 
dim_date_times d ON o.date_uuid = d.date_uuid
GROUP BY 
d.year, d.month
ORDER BY
total_sales DESC
LIMIT 10;