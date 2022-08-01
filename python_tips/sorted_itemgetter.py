from operator import itemgetter
from datetime import datetime

some_response={
    'Snapshots': [
        {
            'DataEncryptionKeyId': 'string',
            'Description': 'string',
            'Encrypted': True,
            'KmsKeyId': 'string',
            'OwnerId': 'string',
            'Progress': 'string',
            'SnapshotId': 'string',
            'StartTime': datetime(2015, 1, 1),
            'State': 'pending',
            'StateMessage': 'string',
            'VolumeId': 'string',
            'VolumeSize': 123,
            'OwnerAlias': 'string',
            'OutpostArn': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'StorageTier': 'archive',
            'RestoreExpiryTime': datetime(2015, 1, 1)
        },
        {
            'DataEncryptionKeyId': 'string',
            'Description': 'string',
            'Encrypted': True,
            'KmsKeyId': 'string',
            'OwnerId': 'string',
            'Progress': 'string',
            'SnapshotId': 'string',
            'StartTime': datetime(2017, 1, 1),
            'State': 'pending',
            'StateMessage': 'string',
            'VolumeId': 'string',
            'VolumeSize': 123,
            'OwnerAlias': 'string',
            'OutpostArn': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'StorageTier': 'archive',
            'RestoreExpiryTime': datetime(2017, 1, 1)
        },
        {
            'DataEncryptionKeyId': 'string',
            'Description': 'string',
            'Encrypted': True,
            'KmsKeyId': 'string',
            'OwnerId': 'string',
            'Progress': 'string',
            'SnapshotId': 'string',
            'StartTime': datetime(2011, 1, 1),
            'State': 'pending',
            'StateMessage': 'string',
            'VolumeId': 'string',
            'VolumeSize': 123,
            'OwnerAlias': 'string',
            'OutpostArn': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'StorageTier': 'archive',
            'RestoreExpiryTime': datetime(2011, 1, 1)
        }                
    ],
    'NextToken': 'string'
}

#sorted() sort iterable
# param1: the iterable to sort | sort the list of dictionaries
# param2: custom key function to customize the sort order | sorts by dict key:'StartTime'
# param3: reverse | sort in descending order
da_sorted = sorted(some_response['Snapshots'], key=itemgetter('StartTime'), reverse=True)

for item in da_sorted:
    print(item['StartTime'])
