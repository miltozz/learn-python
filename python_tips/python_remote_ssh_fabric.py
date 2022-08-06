from fabric import Connection
from invoke import Responder

# set host 'ec2-monitor' in .ssh/config to be read automatically
# else must specify connection details here
result = Connection('ec2-monitor').run('docker ps', hide=True)
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
print(msg.format(result))


# other syntax
c = Connection('ec2-monitor')
r = c.run('sudo whoami', hide=True)
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
print(msg.format(result))


# sudo password prompt
""" c = Connection('host')
sudopass = Responder(
    pattern=r'\[sudo\] password:',
    response='mypassword\n',
)
c.run('sudo whoami', pty=True, watchers=[sudopass]) """
