from flask import jsonify, Response


# Example set of status
STATUS = {
    "version": "1.0.0",
    "status": "healthy",
}


def read_all() -> Response:
    """
    Read and returns all health status, supports HTTP GET.

    :return: All status information
    :rtype: Response
    """
    return jsonify(STATUS)
