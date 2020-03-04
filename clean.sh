#!/bin/bash

docker-compose down > /dev/null 2>&1

docker stop idp_interface_msg > /dev/null 2>&1
docker stop idp_interface > /dev/null 2>&1
docker stop idp_advertise > /dev/null 2>&1
docker stop idp_db > /dev/null 2>&1
docker stop idp_grafana > /dev/null 2>&1

interface_msg=$(docker container ls -a | grep "server_interface_msg" | sed 's/  */ /g' | cut -d' ' -f1)
interface=$(docker container ls -a | grep "server_interface " | sed 's/  */ /g' | cut -d' ' -f1)
advertise=$(docker container ls -a | grep "server_advertise" | sed 's/  */ /g' | cut -d' ' -f1)
mysql=$(docker container ls -a | grep "mysql" | sed 's/  */ /g' | cut -d' ' -f1)
grafana=$(docker container ls -a | grep "grafana" | sed 's/  */ /g' | cut -d' ' -f1)

docker container rm $interface_msg > /dev/null 2>&1
docker container rm $interface > /dev/null 2>&1
docker container rm $advertise > /dev/null 2>&1
docker container rm $mysql > /dev/null 2>&1
docker container rm $grafana > /dev/null 2>&1

interface_msg=$(docker image ls -a | grep "server_interface_msg" | sed 's/  */ /g' | cut -d' ' -f3)
interface=$(docker image ls -a | grep "server_interface " | sed 's/  */ /g' | cut -d' ' -f3)
advertise=$(docker image ls -a | grep "server_advertise" | sed 's/  */ /g' | cut -d' ' -f3)
mysql=$(docker image ls -a | grep "mysql" |  sed 's/  */ /g' | cut -d' ' -f3)
grafana=$(docker image ls -a | grep "grafana" | sed 's/  */ /g' | cut -d' ' -f3)

docker image rm $interface_msg > /dev/null 2>&1
docker image rm $interface > /dev/null 2>&1
docker image rm $advertise > /dev/null 2>&1
docker image rm $mysql > /dev/null 2>&1
docker image rm $grafana > /dev/null 2>&1

rm -rf data

exit 0
