# restore volume from snapshot
# attach volume to instance
# create_volume
'''response = client.create_volume(
    AvailabilityZone='us-east-1a',
    Iops=1000,
    SnapshotId='snap-066877671789bd71b',
    VolumeType='io1',
)'''
# attach_volume
'''response = client.attach_volume(
    Device='/dev/sdf',
    InstanceId='i-01474ef662b89480',
    VolumeId='vol-1234567890abcdef0',
)'''

import boto3

ec2_client = boto3.client('ec2', region_name="eu-central-1")
