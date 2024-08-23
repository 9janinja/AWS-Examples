# Upload a new file
with open('test.jpg', 'rb') as data:
    s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)