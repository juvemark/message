#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A message.taskapp worker -l INFO
