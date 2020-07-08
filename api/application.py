import connexion
import os
import structlog

# Application configuration
APP_API_FILE = os.environ["APP_API_FILE"]
APP_DEBUG_MODE = os.environ["APP_DEBUG_MODE"]
APP_HOST = os.environ["APP_HOST"]
APP_PORT = os.environ["APP_PORT"]
APP_SPEC_DIR = os.environ["APP_SPEC_DIR"]
APP_VERSION = os.environ["APP_VERSION"]

# Logger
logger = structlog.get_logger()

# Create the application instance
app = connexion.App(__name__, specification_dir=APP_SPEC_DIR)

# Read the OpenAPI file to configure the API endpoints
app.add_api(APP_API_FILE, validate_responses=True)

# Run the application in stand alone mode
if __name__ == "__main__":
    logger.info("Starting application")
    app.run(host=APP_HOST, port=APP_PORT, debug=APP_DEBUG_MODE)
