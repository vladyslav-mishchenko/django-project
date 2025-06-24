#!/bin/bash

set -e

source /etc/postgres/postgres-env.sh

# execute the original Postgres entrypoint, passing all args
exec docker-entrypoint.sh "$@"
