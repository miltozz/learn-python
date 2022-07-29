import boto3

#create resource
ec2_resource = boto3.resource('ec2', region_name="eu-central-1")

#create a new vpc. returns created vpc to use subsequently
new_vpc = ec2_resource.create_vpc(
    CidrBlock = "10.0.0.0/16"
)

#create subnet in the new vpc
new_vpc.create_subnet(
    CidrBlock = "10.0.1.0/24"
)

#create another subnet in the new vpc
new_vpc.create_subnet(
    CidrBlock = "10.0.2.0/24"
)
new_vpc.create_tags(
   
    Tags=[
        {
            'Key': 'Name',
            'Value': 'boto created vpc'
        },
    ]
)
