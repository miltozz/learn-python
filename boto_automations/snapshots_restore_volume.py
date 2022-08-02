# Restore volume from latest snapshot and attach it to the instance
#
# Assume ONE volume exists on instance
# Assume we want the latest snapshot
# Assume we have the id of the instance
#
# describe_volumes, get broken volume id
# describe_snapshots, sort get most recent
#
# create_volume from snapshot
# wait for new volume to become avaiable
# attach volume to instance


from operator import itemgetter
from pydoc import describe
import boto3
import time

ec2_client = boto3.client('ec2', region_name="eu-central-1")
ec2_resource = boto3.resource('ec2', region_name="eu-central-1")

instance_id = 'i-0146c0899c6e09c65'


volume = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'tag:env',
            'Values': ['prod', 'staging']
        },
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        },
    ],
)

# ASSUMING just ONE VOLUME in the instance
# We get the id the volume
instance_volume_id = (volume['Volumes'][0]['VolumeId'])

# describe volume snapshots, sort by most recent and get the snapshot's id
snapshots = ec2_client.describe_snapshots(
    Filters=[
        {
            'Name': 'volume-id',
            'Values': [instance_volume_id]
        },
    ],
    OwnerIds=[
        'self',
    ],
)

# sort the list of dictionaries by 'StartTime' and reverse
most_fresh_snap = sorted(
    snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)[0]
print(most_fresh_snap)
print(most_fresh_snap['SnapshotId'])


# create the new volume with tags. az and snapshot id required.
try:
    new_volume = ec2_client.create_volume(
        AvailabilityZone='eu-central-1c',
        SnapshotId=most_fresh_snap['SnapshotId'],
        VolumeType='gp2',
        TagSpecifications=[
            {
                'ResourceType': 'volume',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'prod-volume'
                    },
                    {
                        'Key': 'env',
                        'Value': 'prod'
                    }
                ]
            }
        ]
    )
except Exception as e:
    print(e, e.__class__)

time.sleep(1)  # wait 1s for volume state to become available

# if we don't use the above sleep(1), the volume attachment fails,as it needs some millisecs
# to become available and can be attached.
#
# to be sure we check volume state and when it is 'available' then we go on with the attach
while True:
    vol = ec2_resource.Volume(new_volume['VolumeId'])
    print(vol.state)
    if vol.state == 'available':
        ec2_resource.Instance(instance_id).attach_volume(
            Device='/dev/xvdb',
            VolumeId=new_volume['VolumeId']
        )
        print('\nVolume attached!')
        break
