'''
Use the boto3 library to add 'prod' and 'dev', 'environment' tags to all ec2 instances 
in two different regions: Paris and Frankfurt. 
boto3.client is used to retrieve instance ids which are needed for boto3.resource to create tags. 
Basically repeats same logic for both regions. Not very D.R.Y. but it's OK 8-)
'''

import boto3

# create client. override default region
ec2_client_paris = boto3.client('ec2', region_name="eu-west-3")

# create resource
ec2_resource_paris = boto3.resource('ec2', region_name="eu-west-3")

# create client. override default region
ec2_client_frankfurt = boto3.client('ec2', region_name="eu-central-1")

# create resource
ec2_resource_frankfurt = boto3.resource('ec2', region_name="eu-central-1")

instance_ids_paris = []
instance_ids_frankfurt = []

# add Tag{'Key':'environment', 'Value':'prod'} to all ec2 instances in the region
# client ec2 paris describe_instances() paris. get instance ids and populates list.
# remove jenkins id from list
# resource ec2 paris create_tags, takes ids list and creates tags on th vms
reservations_paris = ec2_client_paris.describe_instances()["Reservations"]  # returns list
for reservation in reservations_paris:  # reservation is dict
    instances = reservation["Instances"]  # instances is list
    for instance in instances:  # instance is dict
        instance_ids_paris.append(instance["InstanceId"])


# Remove ec2-vm of jenkins container from instance_ids_paris
instance_ids_paris.remove("i-0ce8afbe8aa69fabb")
print(instance_ids_paris)


response = ec2_resource_paris.create_tags(
    Resources=instance_ids_paris,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)


# add Tag{'Key':'environment', 'Value':'dev'} to all ec2 instances in the region
# same as above, but for frankfurt region
# no jenkins id removal
reservations_frankfurt = ec2_client_frankfurt.describe_instances()["Reservations"]  # returns list
for reservation in reservations_frankfurt:  # reservation is dict
    instances = reservation["Instances"]  # instances is list
    for instance in instances:  # instance is dict
        instance_ids_frankfurt.append(instance["InstanceId"])


response = ec2_resource_frankfurt.create_tags(
    Resources=instance_ids_frankfurt,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)
