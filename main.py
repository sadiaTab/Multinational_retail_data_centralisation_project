from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

## Create a DatabaseConnector instance
db_connector = DatabaseConnector('db_creds.yaml')
engine = db_connector.init_db_engine()

## Create a DataExtractor instance
data_extractor = DataExtractor(db_connector)
## Create a DataCleaning instance
data_cleaning = DataCleaning(db_connector)

## List all tables in the database
tables = db_connector.list_db_tables(engine)
print("Tables in the database:")
for table in tables:
    print(table)

## Read user table and extract to a dataframe
table_name = "legacy_users"  # Replace with the actual table name
data = data_extractor.read_rds_table(table_name,engine)
## if data is not None:
##     print(f"Data from {table_name}:")
##     print(data)
## Clean user data and upload to database as a table
cleaned_user_data = data_cleaning.clean_user_data(data)
db_connector.upload_to_db(cleaned_user_data, 'dim_user_table')

## Extract card data from pdf
pdfurl='https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf'
card_data = data_extractor.retrieve_pdf_data(pdfurl)
cleaned_card_data = data_cleaning.clean_card_data(card_data)
db_connector.upload_to_db(cleaned_card_data, 'dim_card_details')


## Read stores data
st_data = data_extractor.retrieve_stores_data()
print('st_data ',st_data.shape)
## Clean and upload store data to database as table
cleaned_store_data = data_cleaning.clean_store_data(st_data)
db_connector.upload_to_db(cleaned_store_data, 'dim_store_details')

## Get products data from s3
s3_address = 's3://data-handling-public/products.csv'
product_data = data_extractor.extract_from_s3(s3_address)
## Clean and upload product data to database as table        
cleaned_product_df = data_cleaning.convert_product_weights(product_data)
cleaned_product_data = data_cleaning.clean_products_data(cleaned_product_df)
db_connector.upload_to_db(cleaned_product_data, 'dim_products')
cleaned_product_data.to_csv('cleaned_product_data.csv',index=False)

## Read orders_table
table_name = "orders_table"  # Replace with the actual table name
data = data_extractor.read_rds_table(table_name,engine)
# if data is not None:
#     print(f"Data from {table_name}:")
#     print(data)
## Clean order data and upload to database as a table
clean_order_data = data_cleaning.clean_orders_data(table_name,db_connector)
db_connector.upload_to_db(clean_order_data, 'orders_table')

## Read events data
events_data = data_extractor.extract_from_s3_events()
## Clean events data and upload to database as a table
cleaned_events_data = data_cleaning.clean_events(events_data)
db_connector.upload_to_db(cleaned_events_data, 'dim_date_times3')
