import logging
import boto3
from botocore.exceptions import ClientError


response = client.create_bucket(
    Bucket='examplebucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1',
    },
)

print(response)