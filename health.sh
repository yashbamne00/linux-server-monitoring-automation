#!/bin/bash

echo "WSL Status Below"

echo 

echo "--Cpu usage--"
top -bn1 | head -5

echo

echo "--Ram--"
free -m | head -5

echo

echo "--Disk--"
df -h | head -5
