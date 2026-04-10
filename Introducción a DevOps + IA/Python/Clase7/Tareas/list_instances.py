
import boto3

def list_instances(ec2):
    for instance in ec2.instances.all():
        print(f"Id: {instance.id}")
        print(f"Estado: {instance.state['Name']}")
        print(f"Tipo: {instance.instance_type}")
        print(f"IP pública: {instance.public_ip_address}")
        print("-" * 40)

if __name__=="__main__":
    ec2 = boto3.resource("ec2")
    list_instances(ec2)
