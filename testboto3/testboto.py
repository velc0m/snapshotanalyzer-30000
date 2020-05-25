import boto3

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

if __name__ == '__main__':
    inst = ec2.instances.all()
    print("EC2 instance boto3 type: {}".format(type(inst)))
    print(list(inst))
    inst_1 = list(inst)[0]
    print("Instance id: {}".format(inst_1.id))
    print("Instance placement: {}".format(inst_1.placement))
    print("State placement: {}".format(inst_1.state))
