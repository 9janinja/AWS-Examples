import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the S3 client
s3 = boto3.client('s3')

# Specify the S3 bucket name
bucket_name = 'my-unique-bucket-name-49'

try:
    # List the objects in the bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    # Check if the bucket contains any objects
    if 'Contents' in response:
        print(f"Objects in '{bucket_name}':")
        for obj in response['Contents']:
            print(f" - {obj['Key']}")
    else:
        print(f"The bucket '{bucket_name}' is empty.")
except NoCredentialsError:
    print("AWS credentials not available.")
except PartialCredentialsError:
    print("Incomplete AWS credentials provided.")
except Exception as e:
    print(f"An error occurred: {e}")
