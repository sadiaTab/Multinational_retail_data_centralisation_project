
ALTER TABLE dim_users RENAME TO dim_user_table;

ALTER TABLE dim_user_table
   ALTER COLUMN first_name TYPE VARCHAR(255),
   ALTER COLUMN last_name TYPE VARCHAR(255),
   ALTER COLUMN date_of_birth TYPE DATE,
   ALTER COLUMN country_code TYPE VARCHAR(2), 
   ALTER COLUMN user_uuid TYPE UUID USING user_uuid::uuid,
   ALTER COLUMN join_date TYPE DATE;
   
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'dim_user_table';   