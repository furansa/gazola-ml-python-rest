#!/usr/bin/env bash
#
# @file      entrypoint.sh
# @version   0.0.1
# @brief     Docker entrypoint script
#
# ------------------------------------------------------------------------------
#
# Leave if any command fails
set -e

# Used for debugging if no foreground application is being called
# while true; do
#    date
#    uptime
#    sleep 5
# done

# Call the application in foreground
/usr/bin/env python3 application.py
