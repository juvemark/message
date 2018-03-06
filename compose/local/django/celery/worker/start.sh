#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


celery -A message.taskapp worker -l INFO
