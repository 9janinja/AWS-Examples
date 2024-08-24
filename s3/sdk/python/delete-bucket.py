import logging
import boto3
from botocore.exceptions import ClientError

# Initialize the S3 client
client = boto3.client('s3')

# Prompt for the bucket name
bucket_name = input("Enter Bucket Name: ")

try:
    # Attempt to delete the specified bucket
    client.delete_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' deleted successfully.")
except ClientError as e:
    # Log the error and notify the user
    logging.error(e)
    print(f"Error deleting bucket: {e}")
