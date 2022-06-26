#!/usr/bin/env sh

set -e

export HOST="${HOST:-::}"
export PORT="${PORT:-8080}"

mkdir -p persist/ static/

if [ "$1" = "run" ]; then
  exec uvicorn --workers 2 --host "$HOST" --port "$PORT" \
      --factory "remotegpio.app:create_app"
elif [ "$1" = "startup-test" ]; then
  sleep 5s
  exec uvicorn --workers 1 --host "$HOST" --port "$PORT" \
      --factory "remotegpio.app:create_app"
else
  exec "$@"
fi
