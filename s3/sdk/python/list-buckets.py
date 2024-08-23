# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)