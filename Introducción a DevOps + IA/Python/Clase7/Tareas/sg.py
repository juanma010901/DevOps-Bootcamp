import boto3

def get_default_securitygroup(ec2_resource):
    for sg in ec2_resource.security_groups.limit(10):
        print(f"{sg.id}: {sg.group_name}")

if __name__ == "__main__":
    get_default_securitygroup(boto3.resource("ec2"))
