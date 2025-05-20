#!/bin/bash
sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl enable docker
sduo usermod -aG docker ubuntu
