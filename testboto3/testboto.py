import boto3

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

if __name__ == '__main__':
    instances = ec2.instances.all()
    print("EC2 instance boto3 type: {}".format(type(instances)))
    print(list(instances))
    inst_1 = list(instances)[0]
    print("Instance id: {}".format(inst_1.id))
    print("Instance placement: {}".format(inst_1.placement))
    print("State placement: {}".format(inst_1.state))
    print("Tags: {}".format(inst_1.tags))

    for i in instances:
        print(i)
        for v in i.volumes.all():
            print(v)
