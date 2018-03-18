import boto3
image = boto3.client('image')
image = instance.create_image(
    BlockDeviceMappings=[
        {
            'DeviceName': 'string',
            'VirtualName': 'string',
            'Ebs': {
                'Encrypted': True|False,
                'DeleteOnTermination': True|False,
                'Iops': 123,
                'SnapshotId': 'string',
                'VolumeSize': 123,
                'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1'
            },
            'NoDevice': 'string'
        },
    ],
    Description='string',
    DryRun=True|False,
    Name='string',
    NoReboot=True|False
)