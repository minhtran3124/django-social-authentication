import os
import requests

from app.settings.components.common import (
    ALLOWED_HOSTS
)

# Turn off debugging
DEBUG = False

ALLOWED_HOSTS += []

# Config hosts on cloud environments
ECS_CONTAINER_METADATA_URI = os.environ.get('ECS_CONTAINER_METADATA_URI')

# if not DEBUG and ECS_CONTAINER_METADATA_URI:
if ECS_CONTAINER_METADATA_URI:
    ELB_HEALTHCHECK_HOSTNAMES = [ip for network in
    requests.get(ECS_CONTAINER_METADATA_URI).json()['Networks']

    for ip in network['IPv4Addresses']]
    ALLOWED_HOSTS += ELB_HEALTHCHECK_HOSTNAMES


# If True, the whitelist will not be used and
# all origins will be accepted. Defaults to False.
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [

]
