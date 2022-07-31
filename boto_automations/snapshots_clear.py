'''
Clear snapshots of selected volumes.
Keep 2 newest snapshots for every volume.

!!!IMPORTANT!!!

First filter describe_volumes to get only the volumes whose snapshots we want to delete.
Then iterate the list of volumes, and delete each volume's snapshots.

Always create a volume list first or we could delete all snapshots 
from all volumes except the 2 newer!!

!!!IMPORTANT!!! 
'''

import boto3
import schedule
import time
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name="eu-central-1")

# First describe_volumes filtered by tag to get ONLY the volumes we want
# e.g. only production volumes tagged with env:prod
#
# then for each volume describe_snapshots:
#   filter by OwnerIds(account numbers,self or amazon)
#   filter by volume-id to get snapshots of the volume
#
#   get snapshots, sort by date, keep 2 newer and delete the rest every sunday at 03:00


def clear_snapshots():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:env',
                'Values': ['prod']
            },
        ],
    )

    for volume in volumes['Volumes']:
        snapshots = ec2_client.describe_snapshots(
            Filters=[
                {
                    'Name': 'volume-id',
                    'Values': [volume['VolumeId']]
                },
            ],
            OwnerIds=[
                'self',
            ],
        )

        # sort the list of dictionaries by 'StartTime' and reverse
        sorted_snaps = sorted(snapshots['Snapshots'],
                              key=itemgetter('StartTime'), reverse=True)

        # debug. print unsorted
        print(f"Volume:{volume['VolumeId']}")
        print('Unsorted snapshots list:')

        for snap in snapshots['Snapshots']:
            print(snap['StartTime'])
            print(snap['SnapshotId'])

        print('------------------')

        # debug. print sorted
        print(f"Volume:{volume['VolumeId']}")
        print('Sorted snapshots list:')

        for snap in sorted_snaps:
            print(snap['StartTime'])
            print(snap['SnapshotId'])

        print('------------------')

        # DELETE SNAPSHOTS. skip first two, start from third item
        for snap in sorted_snaps[2:]:
            response = ec2_client.delete_snapshot(
                SnapshotId=snap['SnapshotId']
            )

            print(f"DELETED SNAP:{response}")#feedback on deleted snaps


clear_snapshots()

'''
# uncomment to schedule
#schedule.every().sunday.at("03:00").do(clear_snapshots)

# run scheduled jobs
while True:  # forever
    schedule.run_pending()
    time.sleep(1)
'''