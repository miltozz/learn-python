import boto3

# override default region
ec2 = boto3.client('ec2', region_name='eu-central-1')

# check instance state, status and system status from describe_instance_status
response = ec2.describe_instance_status(
    IncludeAllInstances=True
)

statuses = response["InstanceStatuses"]
for status in statuses:
    print(f"Instance {status['InstanceId']} state is: {status['InstanceState']['Name']} with instance status: {status['InstanceStatus']['Status']} and system status: {status['SystemStatus']['Status']}")
    print("#######")


'''
#list s3.buckets, then list bucket objects and print object Key
s3 = boto3.client('s3', region_name='eu-west-3')
response = s3.list_buckets()
buckets = response["Buckets"]
for bucket in buckets:
    bucket_name = bucket["Name"]
    print(type(bucket_name))
    print(bucket_name)

    response = s3.list_objects_v2(
        Bucket=bucket_name
    )
    contents= response['Contents']
    for b_object in contents:
        print(b_object['Key'])
'''