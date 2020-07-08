from flask import jsonify, request, Response

from ml import linear_regression


def predict() -> Response:
    """
    Return the apartment's price predicted by the model, supports HTTP POST.

    :param dataset: Set of data to feed the model
    :type dataset: Request (JSON)

    :return: Predicted price
    :rtype: Response (JSON)
    """
    dataset = request.json
    model = linear_regression

    return jsonify(model.predict(dataset)), 200
