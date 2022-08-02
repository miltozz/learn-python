'''
Get all volumes with tag env:prod or env:staging and create snapshots.
Add volume id in the created snapshot desription
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
        try:
            snapshot = ec2_client.create_snapshot(
                Description=f"Snapshot of volume:{volume['VolumeId']}",
                VolumeId=volume['VolumeId'],
            )
            print(snapshot)
      
        except Exception as e:
            print(e)
            print(e.__class__)
            print('ERROR: ec2_client.create_snapshot')  



#create_p_s_snapshots()
''' SCHEDULING

#schedule rule
schedule.every().day.at("02:00").do(create_p_s_snapshots)

# run scheduled jobs
while True:  # forever
    schedule.run_pending()
    time.sleep(1)
'''