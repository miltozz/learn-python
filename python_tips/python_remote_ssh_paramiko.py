# execute remote commands via shh with paramiko

from sys import stderr, stdin, stdout
import paramiko


ssh = paramiko.SSHClient()

# known_hosts prompt
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect as ec2-user with .pem | root connection might require priv-key pub-key.pub
ssh.connect(hostname='18.184.246.158',
            username="ec2-user",
            key_filename='/home/mltamd/.ssh/ec2-key-pair-frankfurt.pem')
stdin, stdout, stderr = ssh.exec_command('docker ps')
print(stdout.readlines())
ssh.close()
