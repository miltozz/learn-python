import boto3
import schedule

# override default region
ec2 = boto3.client('ec2', region_name="eu-central-1")

# check instance state, status and system status from describe_instance_status
def check_instance_status():

    response = ec2.describe_instance_status(
        IncludeAllInstances=True
    )
    statuses = response["InstanceStatuses"]
    for status in statuses:
        print(f"Instance {status['InstanceId']} state is: {status['InstanceState']['Name']} with instance status: {status['InstanceStatus']['Status']} and system status: {status['SystemStatus']['Status']}")
        print("#######")

    print("###############################################")


# schedule instance checks
schedule.every(10).seconds.do(check_instance_status)

# schedule some prints
schedule.every(5).seconds.do(print("5 seconds..."))

# run scheduled jobs
while True:  # forever
    schedule.run_pending()
