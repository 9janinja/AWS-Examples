import boto3
s3 = boto3.client('s3')
s3.upload_file(r'C:\Users\BarryAwure\Downloads\HOP School of HArvest (HSH) Training Manual - Module 1.pdf', 'my-unique-bucket-name-49', 'HOP School of HArvest (HSH) Training Manual - Module 1.pdf')


