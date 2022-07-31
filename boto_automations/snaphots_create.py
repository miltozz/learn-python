import boto3
import schedule
from datetime import datetime

prod_instance_ids = []

ec2_client = boto3.client('ec2', region_name="eu-central-1")


# ec2 describe_instances() with tag:env and value prod
# populate list prod_instance_ids
instances = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'tag:env',
            'Values': [
                'prod',
            ]
        },
    ],
)  # returns dict
reservations = (instances["Reservations"])  # returns reservations list
for reservation in reservations:  # reservation is dict
    instances = reservation["Instances"]  # instances is list
    for instance in instances:  # instance is dict
        prod_instance_ids.append(instance['InstanceId'])


# describe_volumes, filter by instance id using the list prod_instance_ids
# create snapshot of each volume, adding description and date
volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': prod_instance_ids,
        },
    ],
)["Volumes"]

for volume in volumes:
    attachments = volume['Attachments']
    for attachment in attachments:
        volume_id = attachment["VolumeId"]
        instance_id = attachment["InstanceId"]
        desc_text = f"Snapshot of Volume with Id:{volume_id} of Instance with Id: {instance_id}"
        now = datetime.now()
        string_now = (str)(now)
        snapshot = ec2_client.create_snapshot(
            Description=desc_text,
            VolumeId=volume_id,
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                    'Tags': [
                        {
                            'Key': 'Instance Id',
                            'Value': instance_id
                        },
                        {
                            'Key': 'Date created',
                            'Value': string_now
                        },
                    ]
                },
            ],
            DryRun=False
        )
