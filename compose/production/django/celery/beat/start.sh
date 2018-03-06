#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A message.taskapp beat -l INFO
