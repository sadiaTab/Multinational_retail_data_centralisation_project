-- SELECT column_name, data_type
-- FROM information_schema.columns
-- WHERE table_name = 'dim_store_details';

-- UPDATE dim_store_details
-- SET longitude = NULL
-- WHERE longitude = 'N/A' OR NOT longitude ~ '^[-+]?[0-9]*\.?[0-9]+$';

-- -- Update invalid entries to NULL for latitude
-- UPDATE dim_store_details
-- SET latitude = NULL
-- WHERE latitude = 'N/A' OR NOT latitude ~ '^[-+]?[0-9]*\.?[0-9]+$';

ALTER TABLE dim_store_details
   ALTER COLUMN longitude TYPE FLOAT USING longitude::double precision,
   ALTER COLUMN locality TYPE VARCHAR(255),
   ALTER COLUMN store_code TYPE VARCHAR(12), 
   ALTER COLUMN staff_numbers TYPE SMALLINT USING staff_numbers::smallint,
   ALTER COLUMN opening_date TYPE DATE,
   ALTER COLUMN store_type TYPE VARCHAR(255),
   ALTER COLUMN latitude TYPE FLOAT USING latitude::double precision,
   ALTER COLUMN country_code TYPE VARCHAR(2), 
   ALTER COLUMN continent TYPE VARCHAR(255);