#!/bin/bash

current_date_time=$(date +"%y-%m-%d %H:%M:%S")

username=$(whoami)

log_file="user_activity.log"
custom_message="Already log."
echo "$current_date_time - $username: $custom_message" >> "$log_file" 
echo "this will be appended to the file" >> user_activity_log.txt


###########################################
#|      Script created by Dcman          |#
###########################################