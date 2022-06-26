#!/usr/bin/env bash -e

cd "$(dirname "$0")"

if [[ $EUID -ne 0 ]]; then
    echo "You need to run this using sudo or as root."
    exit 1
fi

cp remotegpio.service /usr/lib/systemd/system/
systemctl daemon-reload
systemctl enable remotegpio
