# -*- coding: utf-8 -*-

"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings
To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""

from os import environ

from split_settings.tools import include

# Managing environment via DJANGO_ENV variable:
environ.setdefault('DJANGO_ENV', 'local')
ENV = environ['DJANGO_ENV']

base_settings = [
    'components/common.py',
    'components/logging.py',
    'components/database.py',
    'components/authentication.py',

    # You can even use glob:
    # 'components/*.py'

    # Select the right env:
    'environments/{0}.py'.format(ENV),

    # include third party configurations at here
    'third_parties/gcloud.py',
]

# Include settings:
include(*base_settings)
