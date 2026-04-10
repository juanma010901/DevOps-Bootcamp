import boto3

def terminate_instance(ec2_client):
    response = ec2_client.terminate_instances(
        InstanceIds=[
            'i-0835c6ebc4591d952',  # Change here the InstanceID
        ],
        DryRun=False
    )

    print(response)

if __name__ == "__main__":
    ec2_client = boto3.client('ec2')
    terminate_instance(ec2_client)
