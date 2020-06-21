import os

from flask import jsonify, Response


APP_VERSION = os.environ["APP_VERSION"]

STATUS = {
    "version": APP_VERSION,
    "status": "healthy",
}


def read_all() -> Response:
    """
    Read and return all health status, supports HTTP GET.

    :return: All status information
    :rtype: Response (JSON)
    """
    return jsonify(STATUS)
