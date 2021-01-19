#!/bin/bash
set -e

echo "Sensor starting..."
echo "127.0.0.1 $HOSTNAME" >> /etc/hosts

python3 main.py
