#!/usr/bin/env bash

set -e

cd "$(dirname "$0")"

source venv/bin/activate
export PORT=8000
./run.py
