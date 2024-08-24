import boto3
from botocore.exceptions import ClientError, NoCredentialsError, PartialCredentialsError

# Initialize the S3 client
s3 = boto3.client('s3')

# Function to delete all objects in a bucket
def delete_bucket_objects(bucket_name):
    try:
        # List all objects in the bucket
        response = s3.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in response:
            for obj in response['Contents']:
                print(f"Deleting {obj['Key']} from {bucket_name}")
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
            
            print(f"All objects deleted from bucket '{bucket_name}'.")
        else:
            print(f"No objects to delete in bucket '{bucket_name}'.")

    except ClientError as e:
        print(f"Error deleting objects in bucket '{bucket_name}': {e}")

# Function to delete all S3 buckets
def delete_all_buckets():
    try:
        # List all buckets in the account
        response = s3.list_buckets()
        buckets = response['Buckets']
        
        if not buckets:
            print("No buckets found.")
            return
        
        for bucket in buckets:
            bucket_name = bucket['Name']
            print(f"Processing bucket: {bucket_name}")
            
            # Delete all objects in the bucket
            delete_bucket_objects(bucket_name)
            
            # Attempt to delete the bucket
            try:
                s3.delete_bucket(Bucket=bucket_name)
                print(f"Bucket '{bucket_name}' deleted successfully.")
            except ClientError as e:
                print(f"Error deleting bucket '{bucket_name}': {e}")
            except Exception as e:
                print(f"An unexpected error occurred while deleting bucket '{bucket_name}': {e}")

    except NoCredentialsError:
        print("AWS credentials not available.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials provided.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to delete all buckets
delete_all_buckets()
