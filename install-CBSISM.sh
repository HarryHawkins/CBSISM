#!/bin/bash
#this install script is built for Ubuntu, however it can easily be changed. Simply modify the Docker download link to point to the release for your OS
#install latest docker https://docs.docker.com/engine/install/ubuntu/
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
#install python if not installed
sudo apt-get install python3
sudo apt-get install -y python3-pip # install pip (package manager)
pip3 install virtualenv #install venv to install all required packages for the system
#create virtual environment
virtualenv CBSISM
. CBSISM/bin/activate
pip install -r requirements.txt 
#install docker containers
cd CBSISM/configuration/scripts/dockerScripts
#create prometheus docker image from Dockerfile
docker build -t prometheus .
docker volume create prometheus #create persistent volume
#run prometheus from created image
docker run -d -p 9090:9090 --name prometheus  --ip 172.17.0.4 --mount source=prometheus,target=/prometheus prometheus
#run  grafana container
docker run -d -p 3000:3000 grafana/grafana
#run timescaledb container
#https://docs.timescale.com/timescaledb/latest/how-to-guides/install-timescaledb/self-hosted/docker/installation-docker/#docker-hub
docker run -d --name timescaledb -p 5432:5432 -e POSTGRES_PASSWORD=password timescale/timescaledb:x.y.z-pg:pg_version:
cd ../../../
python3 manage.py runserver

