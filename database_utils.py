import yaml
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import text

class DatabaseConnector:
    def __init__(self, yaml_file='db_creds.yaml'):
        self.yaml_file = yaml_file
    def read_db_creds(self):
        try:
            with open(self.yaml_file, 'r') as file:
                data_loaded = yaml.safe_load(file)
            # print(data_loaded)
            return data_loaded
        except:
            return None

    def init_db_engine(self):
        db_creds = self.read_db_creds()
        if db_creds is not None:
            # print(db_creds)
            DATABASE_TYPE = 'postgresql'
            DBAPI = 'psycopg2'
            HOST = db_creds['RDS_HOST']
            USER = db_creds['RDS_USER']
            PASSWORD = db_creds['RDS_PASSWORD']
            DATABASE = db_creds['RDS_DATABASE']
            PORT = db_creds['RDS_PORT']
            engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}",isolation_level="READ COMMITTED")
            # print(engine)
            return engine
        else:
            print("Error reading database credentials from the YAML file.")
            return None
        
    def list_db_tables(self,engine):
        inspector = inspect(engine)
        return inspector.get_table_names()
    
    def upload_to_db(self, df, table_name):
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = 'localhost'
        USER = 'postgres'
        PASSWORD = '...'
        DATABASE = 'sales_data'
        PORT = 5432
        local_engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        # df.to_sql(table_name, local_engine, if_exists='replace')
        try:
            df.to_sql(table_name, local_engine, index=False, if_exists='replace')
            print(f"Data uploaded to {table_name} successfully.")
        except Exception as e:
            print(f"Error uploading data to {table_name}: {e}")
       




