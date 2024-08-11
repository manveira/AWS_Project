import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 's3demomanve'

    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            objects = [obj['Key'] for obj in response['Contents']]
        else:
            objects = []
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'bucket': bucket_name,
                'objects': objects
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }