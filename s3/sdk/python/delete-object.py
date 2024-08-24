import boto3

# Initialize the S3 client
client = boto3.client('s3')

response = client.delete_objects(
    Bucket='my-unique-bucket-name-49',
    Delete={
        'Objects': [
            {
                'Key': 'HOP School of HArvest (HSH) Training Manual - Module 1.pdf',
            },
            {
                'Key': 'uploads/Arinze Network And Cyber-Security FY 2022 Mission Plan.pptx',
            },
            {
                'Key': 'uploads/Docker Cheat Sheet  LT.pdf',
            },
            {
                'Key': 'uploads/KodeKloud-Kubernetes+-CKAD.pdf',
            },
        ],
        'Quiet': False,
    },
)

print(response)