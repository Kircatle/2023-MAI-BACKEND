#!/bin/bash
# set -o errexit
# set -o pipefail
# set -o nounset

readonly WORKERS_CNT=2

function main()
{
  if ! gunicorn --workers ${WORKERS_CNT} simple_app:application  -b :8002; then
    echo "Failed to run gunicorn..."
    return 1
  fi
}

main $@