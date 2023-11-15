SELECT ROUND(SUM(o.product_quantity * p.product_price)::numeric, 2) as total_sales,
s.store_type AS store_type, s.country_code AS country_code
FROM orders_table o
JOIN
	dim_store_details s
ON 
	s.store_code = o.store_code
	JOIN 
	dim_products p 
ON 
	o.product_code = p.product_code
WHERE s.country_code='DE'
GROUP BY store_type, country_code
ORDER BY total_sales
;
