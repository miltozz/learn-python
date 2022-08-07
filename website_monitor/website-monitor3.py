'''
Monitor if an NGINX docker container app, is running. 
Check the status code from GET, API request.

If connected and 200, do nothing.
If connected and !200, restart the container.
If not connected, restart server and then container.

Server is configured to automatically start docker on boot.

boto3 for ec2 interactions
paramiko for remote ssh commands into ec2


IMPROVE:
1. Lots of debugging prints. Can be cleaned.
2. Some DRY code exists. Could be optimized. 
   e.g. paramiko ssh connections or get_host_() functions
3. add aws region in constants
'''

import requests
import smtplib
import os
import paramiko
import time
import boto3

# from dotenv import load_dotenv
# load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

HOST_USER = 'ec2-user'  # paramiko host user for ssh
KEY_FILENAME = '/home/mltamd/.ssh/ec2-key-pair-frankfurt.pem'  # paramiko ssh key
CONTAINER_ID = '06b420614a68'  # container id to restart
INSTANCE_ID_LIST = ['i-06fba9c3d9747cd17'] # ec2 instance id list for describe_instance_status
INSTANCE_ID = 'i-06fba9c3d9747cd17'  # ec2 instance id for boto3:ec2_res.Instance
SEP = '--------------------------------'
# GET_ENDPOINT = 'http://35.158.114.162:8080/' #REQUEST endpoint. replaced by get_host_public_dns
# HOST_IP = '35.158.114.162' #host ip for ssh. replaced by get_host_ip


def send_notification(email_content):
    print(email_content)
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        #smtp.sendmail(sender, receiver, message)
        email_content = f"Subject:WEB MONITOR ALERT\n{email_content}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, email_content)

# assume we configured ec2 docker and containerd services to auto start on boot
# check Official Post-Installation steps on Docker Install
def restart_container():
    print(SEP)
    print("Restarting container...")
    ssh = paramiko.SSHClient()

    # known_hosts prompt
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # connect as ec2-user with .pem | root connection might require key and key.pub pair
    ssh.connect(hostname=get_host_ip(),
                username=HOST_USER,
                key_filename=KEY_FILENAME)
    stdin, stdout, stderr = ssh.exec_command(f"docker restart {CONTAINER_ID}")
    print(stdout.readlines())
    print(SEP)
    print('Container restarted!')
    ssh.close()

# deprecated. use stop_and_start_instance
# works but does not alter instance state and status. they remain as running.
# we have to somehow check if reboot is complete, to use it properly.
def reboot_server():
    print("Rebooting server...")
    ssh = paramiko.SSHClient()

    # known_hosts prompt
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # connect as ec2-user with .pem
        ssh.connect(hostname=get_host_ip,
                    username=HOST_USER,
                    key_filename=KEY_FILENAME)
        stdin, stdout, stderr = ssh.exec_command('sudo reboot')
        print(stdout.readlines())
        ssh.close()
        print('Reboot sent. SSH connection closed.')
    except Exception as e:
        print(f"Error: {e}")
        print('Cannot SSH. Is server running?')


def stop_and_start_instance():
    ec2_res = boto3.resource('ec2')
    instance = ec2_res.Instance(INSTANCE_ID)

    print(SEP)
    print("Restart instance..")
    print(f"Instance state: {instance.state}")
    print(f"Public IP: {instance.public_ip_address}")
    print(SEP)

    # instance.stop
    print('Stopping instance...')
    response = instance.stop()
    print('Stop response:')
    print(response)
    print(SEP)

    # instance.wait_until_stopped
    print('Waiting for instance to stop...')
    response = instance.wait_until_stopped()
    print(SEP)

    # start_instance
    print('Starting instance..')
    response = instance.start()
    print('Start response:')
    print(response)
    print(SEP)

    print('Wait until instance is running...')
    # instance.wait_until_running
    response = instance.wait_until_running()
    print(SEP)

    print("Instance Restart complete!")
    print(SEP)
    print(f"Instance state: {instance.state}")
    print(f"Public IP: {instance.public_ip_address}")
    print(SEP)


def wait_for_server_status_and_states_ok():
    print('Waiting for instance/server to be fully initialized..')
    print("Entering wait loop..")
    print(SEP)
    while True:
        ec2 = boto3.client('ec2', region_name='eu-central-1')
        print('Waiting 10 seconds before retry..')
        time.sleep(10)

        # check instance state, status and system status from describe_instance_status
        response = ec2.describe_instance_status(
            IncludeAllInstances=True,
            InstanceIds=INSTANCE_ID_LIST
        )

        server_state = ''
        instance_status = ''
        system_status = ''

        statuses = response["InstanceStatuses"]
        for status in statuses:  # improve :no for, pick it up explicitly
            print(SEP)
            print(f"Instance {status['InstanceId']} state is: {status['InstanceState']['Name']} with instance status: {status['InstanceStatus']['Status']} and system status: {status['SystemStatus']['Status']}")
            print(SEP)
            server_state = status['InstanceState']['Name']
            instance_status = status['InstanceStatus']['Status']
            system_status = status['SystemStatus']['Status']

        if server_state == 'running' and instance_status == 'ok' and system_status == 'ok':
            print(
                "Server fully initialised!  Instance state is running, statuses are ok... exiting waiting loop")
            print(SEP)
            time.sleep(5)
            break


def get_host_ip():
    ec2_res = boto3.resource('ec2')
    instance = ec2_res.Instance(INSTANCE_ID)
    return instance.public_ip_address


def get_host_public_dns():
    ec2_res = boto3.resource('ec2')
    instance = ec2_res.Instance(INSTANCE_ID)
    return instance.public_dns_name


#main logic
try:
    r = requests.get(f"http://{get_host_public_dns()}:8080/")
    if r.status_code == 200:
        print("Website is up!")
    else:
        print("Website is down!")
        # send email
        message = "Website is down!"
        send_notification(message)
        restart_container()
except Exception as e:
    print(f"Connection error: {e}")
    message = "Connection error!"
    send_notification(message)
    print("Attempt to restart server and container. This may take some time...")
    stop_and_start_instance()
    wait_for_server_status_and_states_ok()
    restart_container()
