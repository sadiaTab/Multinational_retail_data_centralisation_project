SELECT country_code, COUNT(*) FROM dim_store_details 
GROUP BY country_code
ORDER BY COUNT(*) DESC
LIMIT 3;