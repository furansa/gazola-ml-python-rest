#!/usr/bin/env python3
#
# @file      health_checker.py
# @version   0.0.1
# @brief     Check application's health without using external tools
#
# ------------------------------------------------------------------------------
#
import json
import urllib.request
import sys


def check_service_status(url: str) -> int:
    """
    Check general service status.

    :param url: Service URL address
    :type url: str

    :return: 0 if healthy, otherwise 1
    :rtype: int
    """
    with urllib.request.urlopen(url, timeout=5) as response:
        http_response_code = response.getcode()
        http_response_data = json.loads(response.read().decode("utf8"))
        service_status = http_response_data["status"]

        if http_response_code == 200 and service_status == "healthy":
            sys.exit(0)

    sys.exit(1)


if __name__ == "__main__":
    """
    Main program entrypoint
    """
    url = "http://localhost:8000/v1/status"

    check_service_status(url)

    sys.exit(1)
