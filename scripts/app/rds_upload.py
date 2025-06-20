from sqlalchemy import create_engine
import pandas as pd
import os
import boto3
from dotenv import load_dotenv
load_dotenv()

# rds_client = boto3.client("rds", 
# aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
# aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
# region_name=os.getenv('AWS_REGION'))

# db_instance_identifier = 'clinical'
# response = rds_client.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)

# # Extract the endpoint address
# rds_endpoint = response['DBInstances']['Endpoint]['Address]

rds_endpoint = 'clinical.cwpmisqy4ng3.us-east-1.rds.amazonaws.com'
database_name = 'postgres'
username = os.getenv('DB_ADMIN_NAME')
password = os.getenv('DB_ADMIN_PASSWORD')

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{rds_endpoint}/{database_name}')

# Read CSVs into DataFrames
files = os.listdir('./preprocessed_data/')
dataframes = {}

for file in files:
    if not file.endswith('.csv'):
        continue
    df = pd.read_csv(os.path.join('./preprocessed_data/', file), low_memory=False)
    table_name = file.replace('.csv', '')
    dataframes[table_name] = df

for table_name in dataframes:
    dataframes[table_name].to_sql(name=table_name, con=engine, if_exists='replace', index=False)


# # Test data upload
# test_df = pd.read_sql('SELECT * FROM clinical', con=engine)
# print(test_df.head())
