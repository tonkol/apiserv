#!/usr/bin/env bash

set -e

docker build \
--rm -t "apiserv-image" .

docker create \
--publish=127.0.0.1:5005:5005 \
--expose 5005 \
--name "apiserv" "apiserv-image"

docker start "apiserv"
