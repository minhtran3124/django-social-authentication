#!/usr/bin/env bash

if [ -z "$DEFAULT_EMAIL" ]; then
    DEFAULT_EMAIL="admin@gmail.com"
    DEFAULT_PASS="abcd1234"
fi

bin/dj.sh migrate

echo "Create super user if does not exist ..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(email='$DEFAULT_EMAIL').exists() or User.objects.create_superuser('$DEFAULT_EMAIL', '$DEFAULT_PASS')" | python src/manage.py shell
