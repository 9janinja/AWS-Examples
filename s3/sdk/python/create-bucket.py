import logging
import boto3
from botocore.exceptions import ClientError

client = boto3.client('s3')

bucket_name = input("Enter Bucket Name: ")
#region = input("Enter Region: ")  # Optional, specify your desired region

try:
    response = client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region,
        },
    )
    print(f"Bucket '{bucket_name}' created successfully.")
except ClientError as e:
    logging.error(e)
    print(f"Error creating bucket: {e}")
else:
    # Print the bucket name
    print(f"Created bucket name: {bucket_name}")
