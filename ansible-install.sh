!# /bin/bash
# Install ansible on Ubuntu

apt-get update -y
apt-get install software-properties-common -y
apt-add-repository ppa:ansible/ansible -y
apt-get update -y
apt-get install ansible -y
