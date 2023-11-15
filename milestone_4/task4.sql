WITH onlinedata AS (
    SELECT 
        COUNT(*) AS numbers_of_sales, 
		SUM(o.product_quantity) AS product_quantity_count, 
		CASE WHEN s.store_type = 'Web Portal' THEN 'Web'
		END AS location
    FROM 
        orders_table o
        JOIN dim_store_details s ON s.store_code = o.store_code
    WHERE 
        s.store_type = 'Web Portal'
	GROUP BY s.store_type
), offlinedata AS(
SELECT 
        COUNT(*) AS numbers_of_sales, 
		SUM(o.product_quantity) AS product_quantity_count, 
		CASE WHEN s.store_type != 'Web Portal' THEN 'Offline'
		END AS location
    FROM 
        orders_table o
        JOIN dim_store_details s ON s.store_code = o.store_code
    WHERE 
        s.store_type != 'Web Portal'
	GROUP BY s.store_type
)

SELECT SUM(numbers_of_sales) AS numbers_of_sales,  
	SUM(product_quantity_count) AS product_quantity_count,location
FROM onlinedata
GROUP BY location
UNION
SELECT SUM(numbers_of_sales) AS numbers_of_sales,
	SUM(product_quantity_count) AS product_quantity_count,location
FROM offlinedata
GROUP BY location
;


