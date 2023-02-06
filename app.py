import os
import boto3
import json
from dotenv import load_dotenv
from datetime import date
load_dotenv()

client = boto3.client(
    's3', 
    endpoint_url=os.getenv('ENDPOINT_URL'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)
obj = client.get_object(
    Bucket=os.getenv('BUCKET_NAME'), 
    Key=f'premier_league/standings/latest.json'
)
data = obj['Body'].read().decode('utf-8')
data_dict = json.loads(data)
rows = data_dict['response'][0]['league']['standings'][0]
for r in rows:
    print(r)

# TODO: 1. figure out what data is necessary and which table it should go to
# TODO: 2. load to Snowflake tables
