import boto3

ec2 = boto3.client('ec2')

lista = ec2.describe_instances(
    Filters=[
        {
            'Name': 'availability-zone',
            'Values': [
                'eu-central-1c'
            ],
        },
    ],
)

# lista1 = ec2.describe_instance_status()

info = [lista]
for l in info:
    print(l)
