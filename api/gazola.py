import connexion
import structlog

# Application configuration
SPEC_DIR = "./"
API_FILE = "openapi.yaml"
APP_HOST = "0.0.0.0"
APP_PORT = 8000
DEBUG_MODE = True

# Logger
logger = structlog.get_logger()

# Create the application instance
app = connexion.App(__name__, specification_dir=SPEC_DIR)

# Read the OpenAPI file to configure the API endpoints
app.add_api(API_FILE)

# Run the application in stand alone mode
# FIXME: Do not run application as root
if __name__ == "__main__":
    logger.info("Starting application")
    app.run(host=APP_HOST, port=APP_PORT, debug=DEBUG_MODE)
