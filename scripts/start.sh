#!/bin/bash
cd /home/ec2-user/devsecops-pipeline
nohup python3 app.py > /tmp/flask.log 2>&1 &
sleep 2
echo "Flask started"