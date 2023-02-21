import boto3

# override default region
ec2 = boto3.client('ec2', region_name="eu-west-3")

# check instance status from boto ec2 describe_instances()
instances = ec2.describe_instances()  # returns dict
reservations = (instances["Reservations"])  # returns reservations list
for reservation in reservations:  # reservation is dict
    instances = reservation["Instances"]  # instances is list
    for instance in instances:  # instance is dict
        print(
            f"Instance with id {instance['InstanceId']} is in state: {instance['State']['Name']}")
        #print(f"Type: {type(instance['Tags'])}") # instance['Tags'] type is list
        for tag in instance['Tags']: # tag is dict
            print(f"TAGS: \n Key: {tag['Key']} \n Value: {tag['Value']}")
        print("#########################")
        