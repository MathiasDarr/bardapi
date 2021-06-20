#!/bin/bash

docker kill bard_postgres_1
docker system prune -f
docker volume prune -f