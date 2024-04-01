import json
import boto3
import pandas as pd
from io import StringIO

def lambda_handler(event, context):
    print(event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    #Use boto3 to get the file
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=bucket, Key=key)
    file_content = response["Body"].read().decode('utf-8')
    
    data = pd.read_json(StringIO(file_content))
    print(data)
    print("redeployed1")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
