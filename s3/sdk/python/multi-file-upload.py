import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the S3 client
s3 = boto3.client('s3')

# List of file paths to upload
file_paths = [
    r'C:\Users\BarryAwure\Downloads\KodeKloud-Kubernetes+-CKAD.pdf',
    r'C:\Users\BarryAwure\Downloads\Telegram Desktop\Docker Cheat Sheet  LT.pdf',
    r'C:\Users\BarryAwure\OneDrive - IT HORIZONS LIMITED\Documents\Mission Plan\Arinze Network And Cyber-Security FY 2022 Mission Plan.pptx'
]

# S3 bucket name
bucket_name = 'my-unique-bucket-name-49'

try:
    for file_path in file_paths:
        # Extract the file name from the file path
        file_name = os.path.basename(file_path)

        # Define the S3 key (i.e., the path and name in S3)
        s3_key = f'uploads/{file_name}'

        # Upload the file
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"File '{file_name}' uploaded to bucket '{bucket_name}' as '{s3_key}'.")
except FileNotFoundError as e:
    print(f"File not found: {e}")
except NoCredentialsError:
    print("AWS credentials not available.")
except PartialCredentialsError:
    print("Incomplete AWS credentials provided.")
except Exception as e:
    print(f"An error occurred: {e}")
