import os
import requests

from app.settings.components.common import (
    ALLOWED_HOSTS
)

# Turn off debugging
DEBUG = True

ALLOWED_HOSTS += [
    'localhost',
    '127.0.0.1',
]

# Config hosts on cloud environments
ECS_CONTAINER_METADATA_URI = os.environ.get('ECS_CONTAINER_METADATA_URI')

# if not DEBUG and ECS_CONTAINER_METADATA_URI:
if ECS_CONTAINER_METADATA_URI:
    ELB_HEALTHCHECK_HOSTNAMES = [ip for network in
    requests.get(ECS_CONTAINER_METADATA_URI).json()['Networks']

    for ip in network['IPv4Addresses']]
    ALLOWED_HOSTS += ELB_HEALTHCHECK_HOSTNAMES
