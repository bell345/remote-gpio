#!/usr/bin/env bash

set -e

cd "$(dirname "$0")"

source venv/bin/activate
export HOST=0.0.0.0
export PORT=8000
./run.py
