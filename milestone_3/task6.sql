ALTER TABLE dim_date_times
	ALTER COLUMN month TYPE VARCHAR(15),
	ALTER COLUMN year TYPE VARCHAR(15),
	ALTER COLUMN day TYPE VARCHAR(15),
	ALTER COLUMN time_period TYPE VARCHAR(15),
	ALTER COLUMN date_uuid TYPE UUID USING date_uuid::uuid;