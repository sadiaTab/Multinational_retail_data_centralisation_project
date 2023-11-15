-- Add foreign key constraint to orders_table referencing other tables
ALTER TABLE orders_table
--card details table
ADD CONSTRAINT fk_card_number
FOREIGN KEY (card_number)
REFERENCES dim_card_details (card_number),
--date times table
ADD CONSTRAINT fk_date_uuid
FOREIGN KEY (date_uuid)
REFERENCES dim_date_times (date_uuid),
--products table
ADD CONSTRAINT fk_product_code
FOREIGN KEY (product_code)
REFERENCES dim_products (product_code),
--store details table
ADD CONSTRAINT fk_store_code
FOREIGN KEY (store_code)
REFERENCES dim_store_details (store_code),
--user table
ADD CONSTRAINT fk_user_uuid
FOREIGN KEY (user_uuid)
REFERENCES dim_user_table (user_uuid);