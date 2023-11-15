SELECT locality, COUNT(*) FROM dim_store_details 
GROUP BY locality
ORDER BY COUNT(*) DESC
LIMIT 7;