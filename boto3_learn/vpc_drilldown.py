import boto3

# override default region
ec2 = boto3.client('ec2', region_name="eu-central-1")

d_response = ec2.describe_vpcs()  # dict
l_vpcs = (d_response["Vpcs"])  # list

for d_vpc in l_vpcs:
    print(d_vpc["VpcId"])
    print(d_vpc["IsDefault"])
    l_cidrBlockAssociationSet = d_vpc["CidrBlockAssociationSet"]

    for d_a_set in l_cidrBlockAssociationSet:
        print(d_a_set["CidrBlock"])
        print(d_a_set["CidrBlockState"])
        print(d_a_set["CidrBlockState"]["State"])
