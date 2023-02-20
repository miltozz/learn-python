import os

# dotenv package
# Mainly for development environments.
# reads env vars from .env file, if exists.

# from dotenv import load_dotenv
# load_dotenv()


# python os package.
# read env vars
print(os.getenv('EMAIL_ADDRESS'))
print(os.getenv('EMAIL_PASSWORD'))
print(os.getenv('DEPLOY'))

print(os.environ.get('EMAIL_ADDRESS'))
print(os.environ.get('EMAIL_PASSWORD'))
print(os.environ.get('DEPLOY'))
print(os.environ['DEPLOY'])
print(os.environ['BACON'])