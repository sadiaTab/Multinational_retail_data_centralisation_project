ALTER TABLE dim_card_details
	ALTER COLUMN card_number TYPE VARCHAR(255),
	ALTER COLUMN expiry_date TYPE VARCHAR(255),
	ALTER COLUMN date_payment_confirmed TYPE DATE USING date_payment_confirmed::date;
	