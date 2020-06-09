from flask import abort, jsonify, Response


# Example set of status
STATUS = {
    "Version": "1.0.0",
    "Status": "healthy",
}


def read_all() -> Response:
    # TODO: Write unit test case (pytest)
    """
    Read and returns all health status, supports HTTP GET.

    :return: All status information
    :rtype: Response
    """
    return jsonify(STATUS)
