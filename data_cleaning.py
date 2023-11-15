import pandas as pd
from dateutil.parser import parse
import numpy as np
from data_extraction import DataExtractor

class DataCleaning:
    def __init__(self, db_connector):
        """
        Initialize the DataCleaning object with a database connector.

        Parameters:
        - db_connector (object): The connector object for the database.
        """
        self.db_connector = db_connector

    def custom_date_parser(self, date_str):
        """
        Custom date parser function.

        Parameters:
        - date_str (str): Date string to be parsed.

        Returns:
        - parsed_date (datetime or np.datetime64): Parsed date or 'NaT' for non-date strings.
        """
        try:
            # Attempt to parse the date
            return parse(date_str)
        except:
            # Return a placeholder for non-date strings
            return np.datetime64('NaT')
        
    def clean_user_data(self,df):
        """
        Clean user data in the DataFrame.

        Parameters:
        - df (DataFrame): Input DataFrame containing user data.

        Returns:
        - cleaned_df (DataFrame): Cleaned user data DataFrame.
        """
        cleaned_df = df.copy()  # Create a copy to avoid modifying the original DataFrame
        cleaned_df = cleaned_df.drop_duplicates()
        cleaned_df.first_name = cleaned_df.first_name.astype('string')
        cleaned_df.last_name = cleaned_df.last_name.astype('string')
        cleaned_df.company= cleaned_df.company.astype('string')
        cleaned_df.email_address= cleaned_df.email_address.astype('string')
        cleaned_df.address= cleaned_df.address.astype('string')
        cleaned_df.country= cleaned_df.country.astype('string')
        cleaned_df.country_code= cleaned_df.country_code.astype('string')
        cleaned_df['country_code'] = cleaned_df['country_code'].replace('GGB','GB')
        cleaned_df.phone_number= cleaned_df.phone_number.astype('string')
        cleaned_df.user_uuid= cleaned_df.user_uuid.astype('string')

        #check for columns that should be date
        cleaned_df['date_of_birth'] = cleaned_df['date_of_birth'].apply(self.custom_date_parser)
        cleaned_df['date_of_birth'] = pd.to_datetime(cleaned_df['date_of_birth'], infer_datetime_format=True, errors='coerce')
        cleaned_df['join_date'] = cleaned_df['join_date'].apply(self.custom_date_parser)
        cleaned_df['join_date'] = pd.to_datetime(cleaned_df['join_date'], infer_datetime_format=True, errors='coerce')
        #drop rows with invalid values for date columns
        cleaned_df = cleaned_df.dropna(subset=['join_date','date_of_birth'])
        cleaned_df.to_csv('cleaned_df.csv')
        return cleaned_df
    
    def clean_card_number(self,card_number):
        """
        Clean card number by removing non-digit characters.

        Parameters:
        - card_number (str): Card number to be cleaned.

        Returns:
        - cleaned_card_number (str): Cleaned card number.
        """
        return ''.join(char for char in str(card_number) if char.isdigit() or char != '?')

    def clean_card_data(self,df):
        """
        Clean card data in the DataFrame.

        Parameters:
        - df (DataFrame): Input DataFrame containing card data.

        Returns:
        - cleaned_df (DataFrame): Cleaned card data DataFrame.
        """
        pdf_dataframe = df[df["card_number"] != "NULL"]
        pdf_dataframe['card_number'] = pdf_dataframe['card_number'].apply(self.clean_card_number)
        pdf_dataframe = pdf_dataframe[pdf_dataframe['card_number'] != '']
        pdf_dataframe = pdf_dataframe[pd.to_numeric(pdf_dataframe['card_number'], errors='coerce').notnull()]
        return pdf_dataframe
    
    def clean_store_data(self,df):
        """
        Clean store data in the DataFrame.

        Parameters:
        - df (DataFrame): Input DataFrame containing store data.

        Returns:
        - cleaned_df (DataFrame): Cleaned store data DataFrame.
        """
        cleaned_df = df.copy()  # Create a copy to avoid modifying the original DataFrame
        cleaned_df.to_csv('store_data_orig.csv')
        cleaned_df.replace({'continent': ['eeEurope', 'eeAmerica']}, {'continent': ['Europe', 'America']}, inplace=True)
        cleaned_df=cleaned_df[cleaned_df['continent'].isin(['America', 'Europe'])]
        cleaned_df['opening_date'] = pd.to_datetime(cleaned_df['opening_date'], infer_datetime_format=True, errors='coerce')
        cleaned_df.drop(columns='lat', inplace=True)
        cleaned_df['staff_numbers'] = cleaned_df['staff_numbers'].str.replace(r'[a-zA-Z]', '', regex=True)
        cleaned_df['staff_numbers'] = pd.to_numeric(cleaned_df["staff_numbers"], errors='coerce')
        cleaned_df["longitude"] = pd.to_numeric(cleaned_df["longitude"], errors='coerce')
        cleaned_df["latitude"] = pd.to_numeric(cleaned_df["latitude"], errors='coerce')
        cleaned_df = cleaned_df.replace('N/A', np.nan)
        cleaned_df = cleaned_df.replace('NULL', np.nan)
        return cleaned_df

    def fix_weird_value(self, value):
        """
        Fix weird value by multiplying two numbers if 'x' is present.

        Parameters:
        - value (str): Input value.

        Returns:
        - fixed_value (str or float): Fixed value.
        """
        if isinstance(value, str) and 'x' in value:
            parts = value.split(' x ')
            try:
                num1 = float(parts[0])
                num2 = float(parts[1])
                return f"{(num1 * num2)}"
            except ValueError:
                pass
        else:
            return value

    def convert_product_weights(self,df):
        """
        Convert product weights in the DataFrame.

        Parameters:
        - df (DataFrame): Input DataFrame containing product weights.

        Returns:
        - df_result (DataFrame): DataFrame with converted product weights.
        """
        df['weight'] = df['weight'].astype(str)
        regex_pattern = r'(?P<weightnumeric>\d+(\.\d+)?)\s*(?P<unit>[a-zA-Z]+)'
        df_extracted = df['weight'].str.extract(regex_pattern)
        # Drop the decimal part column if it exists
        df_extracted.drop(1, axis=1, inplace=True, errors='ignore')
        # Concatenate the extracted columns with the original DataFrame
        df_result = pd.concat([df, df_extracted], axis=1)
        df_result['weightnumeric'] = pd.to_numeric(df_result['weightnumeric'], errors='coerce')  # Convert to numeric, handle non-numeric values as NaN
        df_result['weightnumeric'] = df_result['weightnumeric'].apply(self.fix_weird_value)
        # Update 'weightnumeric' column based on conditions
        df_result['weight'] = df_result.apply(lambda x: x['weightnumeric']/1000 if x['unit']=='g' or x['unit']=='ml' else x['weightnumeric'], axis=1)
        df_result.drop(columns=['weightnumeric','unit'], inplace=True)
        return df_result
    
    def clean_products_data(self,products_dataframe):
        products_df=products_dataframe
        products_df.dropna(subset=['uuid', 'product_code','removed'], inplace=True)
        products_df['date_added']=pd.to_datetime(products_df['date_added'], format='%Y-%m-%d', errors='coerce')
        drop_prod_list=['S1YB74MLMJ','C3NCA2CL35', 'WVPMHZP59U']# list of strings to drop rows for in the next line
        products_df.drop(products_df[products_df['category'].isin(drop_prod_list)].index, inplace=True)# drop the rows where the category column has entries equal to thouse in the list above
        return products_df
    
    def clean_orders_data(self,table_name,db_connector):
        print(table_name)
        data_extractor = DataExtractor(db_connector)
        engine = db_connector.init_db_engine()
        df = data_extractor.read_rds_table(table_name, engine)
        df.drop(columns=['first_name','last_name','1','level_0'],inplace=True)
        return df
    
    def clean_events(self,df):
        date_time_dataframe = df.copy()
        # Convert 'day' to numeric
        date_time_dataframe['day'] = pd.to_numeric(date_time_dataframe['day'], errors='coerce')
        # Drop rows with missing values in 'day', 'year', and 'month'
        date_time_dataframe.dropna(subset=['day', 'year', 'month'], inplace=True)
        # Format 'year', 'month', 'day' as zero-padded integers and concatenate
        date_time_dataframe['datetime'] = pd.to_datetime(
            date_time_dataframe[['year', 'month', 'day']].astype(int).astype(str).agg(' '.join, axis=1) +
            ' ' + date_time_dataframe['timestamp'],
            format='%Y %m %d %H:%M:%S'
        )
        # Convert specific columns to string type
        date_time_dataframe = date_time_dataframe.astype({"timestamp": "string", "time_period": "string", "date_uuid": "string"})
        return date_time_dataframe

