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


def send_notification(email_content):
        print(email_content)
"""     with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        #smtp.sendmail(sender, receiver, message)
        email_content = f"Subject:WEB MONITOR ALERT\n{email_content}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, email_content) """

# assume we configured ec2 docker and containerd services to auto start on boot
# check Official Post-Installation steps on Docker Install
def restart_container():
    print("Restarting container...")
    ssh = paramiko.SSHClient()

    # known_hosts prompt
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # connect as ec2-user with .pem | root connection might require key and key.pub pair
    ssh.connect(hostname='18.192.106.193',
                username="ec2-user",
                key_filename='/home/mltamd/.ssh/ec2-key-pair-frankfurt.pem')
    stdin, stdout, stderr = ssh.exec_command('docker start 06b420614a68')
    print(stdout.readlines())
    ssh.close()

def reboot_server():
    print("Rebooting server...")
    ssh = paramiko.SSHClient()

    # known_hosts prompt
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # connect as ec2-user with .pem | root connection might require key and key.pub pair
    ssh.connect(hostname='18.192.106.193',
                username="ec2-user",
                key_filename='/home/mltamd/.ssh/ec2-key-pair-frankfurt.pem')
    stdin, stdout, stderr = ssh.exec_command('sudo reboot')
    print(stdout.readlines())
    ssh.close()
    print('------------ssh closed--------------')    



def stop_and_start_server():
    ec2_res = boto3.resource('ec2')
    instance = ec2_res.Instance('i-06fba9c3d9747cd17') 






def wait_for_server_status_and_states_ok():
    print('Waiting server to be up..')
    while True:
        ec2 = boto3.client('ec2', region_name='eu-central-1')
        print('Waiting 10..')
        time.sleep(10)
        
        # check instance state, status and system status from describe_instance_status
        response = ec2.describe_instance_status(
            IncludeAllInstances=True,
            InstanceIds=[
                'i-06fba9c3d9747cd17',
            ]
        )

        server_state = ''
        instance_status = ''
        system_status = ''
        
        statuses = response["InstanceStatuses"]
        for status in statuses: #improve :no for, pick it up explicitly
            print(f"Instance {status['InstanceId']} state is: {status['InstanceState']['Name']} with instance status: {status['InstanceStatus']['Status']} and system status: {status['SystemStatus']['Status']}")
            print("#######")
            server_state = status['InstanceState']['Name']
            instance_status = status['InstanceStatus']['Status']
            system_status = status['SystemStatus']['Status']

        if server_state == 'running' and instance_status == 'ok' and system_status == 'ok':
            print("Server is up...exiting waiting loop")
            time.sleep(2)
            break

   

try:
    r = requests.get(
        'http://ec2-18-192-106-193.eu-central-1.compute.amazonaws.com:8080/')
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
    reboot_server()
    wait_for_server_status_and_states_ok()
    restart_container()


