ALTER TABLE dim_products
RENAME COLUMN removed TO still_available;

-- Update values in the still_available column
UPDATE dim_products
SET still_available = CASE WHEN still_available = 'still_available' THEN true ELSE false END;

ALTER TABLE dim_products
   ALTER COLUMN product_price TYPE FLOAT USING product_price::double precision,
   ALTER COLUMN weight TYPE FLOAT,
   ALTER COLUMN "EAN" TYPE VARCHAR(120), 
   ALTER COLUMN product_code TYPE VARCHAR(12),
   ALTER COLUMN date_added TYPE DATE,
   ALTER COLUMN uuid TYPE UUID USING uuid::uuid,
   ALTER COLUMN still_available TYPE BOOLEAN USING still_available::BOOLEAN,
   ALTER COLUMN weight_class TYPE VARCHAR(15);