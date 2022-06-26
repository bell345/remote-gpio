#!/usr/bin/env bash

cd "$(dirname "$0")"

if ! (systemctl status gpio 2>/dev/null); then
    ./install.sh
fi

systemctl start remotegpio
