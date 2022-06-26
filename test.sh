#!/usr/bin/env bash

source venv/bin/activate
python3 -m pytest --color=yes test/ --junit-xml=report.xml $@
