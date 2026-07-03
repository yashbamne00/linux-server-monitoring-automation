#!/bin/bash

find /var/log -type f -mtime +10 -delete
