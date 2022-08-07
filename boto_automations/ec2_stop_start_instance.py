'''
AWS EC2 Instance interactions with boto3 library
'''

import boto3

ec2_res = boto3.resource('ec2')
instance = ec2_res.Instance('i-06fba9c3d9747cd17')  # instance id


def reboot_instance():
    # instance.reboot
    print('reboot_instance')
    response = instance.reboot()
    print('reboot response:')
    print(response)


def stop_instance():
    print('stop_instance')
    # instance.stop
    response = instance.stop()
    print('stop response:')
    print(response)


def start_instance():
    # start_instance
    print('start_instance')
    response = instance.start()
    print('start response:')
    print(response)


def wait_instance_run():
    print('wait_instance_run')
    # instance.wait_until_running
    response = instance.wait_until_running()
    print('wait_instance_run response:')
    print(response)


def wait_instance_stop():
    # instance.wait_until_stopped
    print('wait_instance_stop')
    response = instance.wait_until_stopped()
    print('wait_instance_stop response:')
    print(response)


print(instance.state)
print(instance.public_ip_address)

stop_instance()
wait_instance_stop()

print(instance.state)

start_instance()
wait_instance_run()

print(instance.state)
print(instance.public_ip_address)
