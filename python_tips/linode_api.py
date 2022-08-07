#Needs cleaning

#restart linode server
import linode_api4 #pip install linode-api4
import os
import paramiko
import time


LINODE_TOKEN = os.getenv('LINODE_TOKEN') #env var for LINODE ACCESS TOKEN


def restart_container():
    ssh = paramiko.SSHClient()

    # known_hosts prompt
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # connect as ec2-user with .pem | root connection might require priv-key pub-key.pub
    ssh.connect(hostname='18.184.246.158',
                username="ec2-user",
                key_filename='/home/mltamd/.ssh/ec2-key-pair-frankfurt.pem')
    stdin, stdout, stderr = ssh.exec_command('docker start 06b420614a68')
    print(stdout.readlines())
    ssh.close()


#restart linode server
client = linode_api4.LinodeClient(LINODE_TOKEN)
nginx_server = client.load(linode_api4.Instance, 123456789) #linode server id
nginx_server.reboot()

#restart the app container
while True:
    nginx_server = client.load(linode_api4.Instance, 123456789) #linode server id
    time.sleep(5)
    if nginx_server.status == 'running':
        time.sleep(10)
        restart_container()
        break
