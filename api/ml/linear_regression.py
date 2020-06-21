import structlog

from typing import Dict

# Logger
logger = structlog.get_logger()


def predict(dataset: Dict) -> Dict:
    """
    Mocked function to simulate the result of a prediction model.

    :param dataset: Set of data to feed the model
    :type dataset: Dict

    :return: Predicted price
    :rtype: Dict
    """
    logger.info("Starting prediction")

    RESULT = {
        "price": 999.99,
    }

    return RESULT
