#!/bin/bash
docker-compose down
docker container prune -f
#docker volume prune -f
#docker image prune -f
docker volume create --name=influxdb-storage
docker-compose up --build

