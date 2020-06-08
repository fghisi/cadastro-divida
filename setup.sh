#!/usr/bin/env bash

sudo apt-get update
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update

sudo apt-get install -y python3.5
sudo apt-get install python3.5 python3.5-dev
sudo curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python3.5
sudo easy_install pip
sudo pip3 install bottle
sudo pip3 install PyJWT
