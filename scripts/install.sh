#!/bin/bash
yum update -y
yum install -y python3 python3-pip
pip3 install -r /home/ec2-user/devsecops-pipeline/requirements.txt