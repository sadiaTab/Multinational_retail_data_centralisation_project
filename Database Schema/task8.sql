-- add primary key for table dim_card_details
ALTER TABLE dim_card_details
ADD PRIMARY KEY (card_number)

-- add primary key for table 
ALTER TABLE dim_user_table
ADD PRIMARY KEY (user_uuid)

-- add primary key for table dim_date_times
ALTER TABLE dim_date_times
ADD PRIMARY KEY (date_uuid)

-- add primary key for table dim_products
ALTER TABLE dim_products
ADD PRIMARY KEY (product_code)

-- add primary key for table dim_store_details
ALTER TABLE dim_store_details
ADD PRIMARY KEY (store_code)