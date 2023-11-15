WITH total AS (
	SELECT SUM(o.product_quantity * p.product_price) AS total_sum
FROM
	orders_table o
JOIN 
	dim_products p 
ON 
	o.product_code = p.product_code	
)

SELECT s.store_type, 
	ROUND(SUM(o.product_quantity * p.product_price)::numeric, 2) as total_sales,
	ROUND((SUM(o.product_quantity * p.product_price)/total.total_sum*100)::numeric, 2) AS "percentage_total (%)"	
FROM 
   orders_table o
JOIN
	dim_store_details s
ON 
	s.store_code = o.store_code
JOIN 
	dim_products p 
ON 
	o.product_code = p.product_code	
CROSS JOIN total 
GROUP BY s.store_type, total.total_sum	
ORDER BY total_sales
DESC
;