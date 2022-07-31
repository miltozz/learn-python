'''
Get all volumes with tag env:prod or env:staging and create snapshots.
Schedule snapshot creation every day at 02:00
'''

import boto3
import schedule
import time

ec2_client = boto3.client('ec2', region_name="eu-central-1")

# describe_volumes, filter by instance id using the list prod_instance_ids
# create snapshot of each volume, adding description and date
def create_p_s_snapshots():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:env',
                'Values': ['prod', 'staging'],
            },
        ],
    )

    for volume in volumes['Volumes']:
        snapshot = ec2_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )
        print(snapshot)

#uncomment to schedule
#schedule.every().day.at("02:00").do(create_p_s_snapshots)

# run scheduled jobs
while True:  # forever
    schedule.run_pending()
    time.sleep(1)
