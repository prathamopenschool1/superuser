#!/bin/bash

echo "enter file name with extension: "
read filename
while IFS=, read -a row; do
    username=${row[0]}
    password=${row[1]}
    sudo kolibri manage shell -c "from kolibri.auth.models import FacilityUser; FacilityUser.objects.create_superuser('$username', '$password')"
    done < $filename

echo "all the users have been created"
