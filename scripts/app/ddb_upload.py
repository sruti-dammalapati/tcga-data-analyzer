import json
import boto3
import os
from dotenv import load_dotenv
load_dotenv()

def upload_json_to_dynamodb(json_file_path, table_name):
    session = boto3.Session(aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                  aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                                  region_name=os.getenv('AWS_REGION'))
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table(table_name)
    
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    for item in data:
        if not item.get('case_id'):
            print(f"Skipping item without case_id: {item}")
            continue
        table.put_item(Item=item)
        print(f"Uploaded item with case_id {item['case_id']}")

upload_json_to_dynamodb('./preprocessed_data/biospecimen.project-tcga-lgg.2025-06-14.json', 'biospecimen')