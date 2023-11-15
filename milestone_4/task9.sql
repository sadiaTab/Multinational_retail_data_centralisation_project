WITH TimeDifferences AS (
  SELECT
    d.year AS year,
    LEAD(datetime) OVER (PARTITION BY year ORDER BY datetime ASC) - datetime AS duration
  FROM
    dim_date_times d
)

SELECT
  year,
  CONCAT(
  '{"hours": ', FLOOR(AVG(EXTRACT(EPOCH FROM TimeDifferences.duration)) / 3600),
	', "minutes": ', FLOOR(MOD(CAST(AVG(EXTRACT(EPOCH FROM TimeDifferences.duration)) AS NUMERIC),3600)/60),
	', "seconds": ', FLOOR(MOD(CAST(AVG(EXTRACT(EPOCH FROM TimeDifferences.duration)) AS NUMERIC),60)),
	', "miliseconds": ', ROUND(MOD(CAST(AVG(EXTRACT(EPOCH FROM TimeDifferences.duration)) AS NUMERIC),1) * 1000),
	' }') AS avg_sales_duration,
  AVG(EXTRACT(EPOCH FROM TimeDifferences.duration)) AS avg_sales_duration_seconds
FROM
  TimeDifferences
GROUP BY
  year
ORDER BY
  avg_sales_duration_seconds DESC;
 
