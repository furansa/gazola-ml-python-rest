import os

from flask import jsonify, Response


# Example set of status
APP_VERSION = os.environ["APP_VERSION"]

STATUS = {
    "version": APP_VERSION,
    "status": "healthy",
}


def read_all() -> Response:
    """
    Read and returns all health status, supports HTTP GET.

    :return: All status information
    :rtype: Response
    """
    return jsonify(STATUS)
