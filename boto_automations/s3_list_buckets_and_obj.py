import boto3

s3 = boto3.client('s3', region_name='eu-west-3')

# list s3.buckets, then list bucket objects and print object Key
response = s3.list_buckets()
buckets = response["Buckets"]
for bucket in buckets:
    bucket_name = bucket["Name"]
    print(bucket_name)

    response = s3.list_objects_v2(
        Bucket=bucket_name
    )
    contents = response['Contents']
    for b_object in contents:
        print(b_object['Key'])
