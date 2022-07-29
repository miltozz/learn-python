import boto3

# override default region
ec2 = boto3.client('ec2', region_name="eu-central-1")

# check instance state, status and system status from describe_instance_status
response = ec2.describe_instance_status(
    IncludeAllInstances=True
)

statuses = response["InstanceStatuses"]
for status in statuses:
    print(f"Instance {status['InstanceId']} state is: {status['InstanceState']['Name']} with instance status: {status['InstanceStatus']['Status']} and system status: {status['SystemStatus']['Status']}")
    print("#######")
