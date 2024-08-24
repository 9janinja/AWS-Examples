import boto3
# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Sort buckets by creation date in descending order
sorted_buckets = sorted(response['Buckets'], key=lambda bucket: bucket['CreationDate'], reverse=True)

# Output the names of the 5 most recently created buckets
print('5 Most Recently Created Buckets:')
for bucket in sorted_buckets[:5]:
    print(f'  {bucket["Name"]}')
