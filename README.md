# Multinational Retail Data Centralization Project

## Description

This project aims to centralize and clean data from a multinational retail company, enabling efficient analysis and business decision-making. The data, initially scattered across various sources, is consolidated into a centralized database, serving as a single source of truth for sales data. The project involves an Extract, Transform, Load (ETL) process, including data cleaning, database schema development, and SQL querying to obtain up-to-date business metrics.

## Milestone 1: Set up the environment

Used GitHub to track changes to my code and saved them online in a GitHub repo. 

## Milestone 2: Extracted and cleaned up data from the data sources

- Set up a local database named `sales_data` to store data.
- Created three Python scripts for data_extraction.py, data_cleaning.py, database_utils.py, each with its own class.

- Data Extraction: Implemented methods in the data extraction class to pull data from various sources like CSV files, an API, and an S3 bucket.

- User Data Handling: Developed functions in the `DataExtractor` and `DatabaseConnector` classes to clean and extract user data, handle credentials, and access an AWS RDS database. Performed thorough cleaning of user data in the `DataCleaning` class, addressing issues like NULL values, date errors, and incorrect data types.

- Card Details: Used `DataExtractor` to fetch card details from an AWS S3 bucket stored in a PDF, cleaned the data, and uploaded it to the `sales_data` database.

- Store Data: Retrieved store data through an API, cleaned it, and uploaded the dataframe to the `sales_data` database.

- Product Information: Downloaded and extracted information about products stored in a CSV format on AWS S3 using `DataExtractor`, cleaned the dataframe, and uploaded it to the database.

- Orders Data: Extracted and cleaned the orders table from an AWS RDS database, uploading the dataframe to the database.

- JSON File Extraction: Extracted data from a JSON file on S3 containing sale details, cleaned it, and uploaded the data to the database.

## Milestone 3: Create the database schema

In this milestone, the focus was on ensuring the accuracy of tables within the `sales_database`—confirming correct columns and appropriate data types.

- **Column Alignment:**
   Ensured that all tables within `sales_database` had the correct columns, and data types were accurately cast.

- **Primary Keys Addition:**
   Added primary keys to all dimension tables. Tables prefixed with "dim" were equipped with primary keys to establish unique identifiers.

- **Foreign Key Integration:**
   Established foreign keys in the `orders_table` that referenced the primary keys in the other tables. This interlinking created a cohesive relationship within the database.

- **SQL Implementation:**
   Utilized SQL to create the necessary foreign key constraints, solidifying the star-based database schema. This enhancement ensures data integrity and enables efficient querying for analytical purposes.


## Milestone 4: Querying the data

Wrote SQL queries to answer following questions: 

task_1.sql : How many stores does the business have and in which countries?

task_2.sql : Which locations currently have the most stores?

task_3.sql : Which months produce the most sales typically?

task_4.sql : How many sales are coming from online?

task_5.sql : What percentage of sales come through each type of store?

task_6.sql : Which month in each year produced the most sales?

task_7.sql : What is our staff headcount?

task_8.sql : Which German store type is selling the most?

task_9.sql : How quickly is the company making sales?

## Requirements

Make sure you have the following dependencies installed before running the project:

- [Pandas](https://pandas.pydata.org/): `pip install pandas`
- [SQLAlchemy](https://www.sqlalchemy.org/): `pip install SQLAlchemy`
- [Psycopg2](https://www.psycopg.org/): `pip install psycopg2`
- [Tabula-py](https://github.com/chezou/tabula-py): `pip install tabula-py`
- [Requests](https://docs.python-requests.org/en/latest/): `pip install requests`
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html): `pip install boto3`


