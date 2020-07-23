# Gazola Machine Learning REST API
![Smoke test](https://github.com/furansa/gazola-ml-python-rest/workflows/Smoke%20test/badge.svg?branch=master)

This RESTful Web service provides endpoints to access a Machine Learning model
trained to predict apartment's prices in São Paulo city, based on some features
like total area.

The model was trained using Gazola apartment's prices dataset, and this is an
academic project part of my post graduation course in Artificial Intelligence
and Machine Learning.

Along with the prediction endpoint it's also available a specific endpoint for
the model documentation and a Swagger/OpenAPI interface as well.

The system is deployed using Docker to make it self-contained and allow
scalability across multiple environments.

This is currently a **work in progress**.

## Running
To build and run the application, clone the repository and run in a terminal
from the same directory where the ```docker-compose-{environment}.yaml``` file
is, where *environment* can be *dev*, *test*, *prod* or whatever:

```shell
$ docker-compose -f docker-compose-dev.yaml up
```

To stop the application, run from the same directory:

```
$ docker-compose stop
```

## Accessing
After build and run it's possible to explore the API by using the Swagger/OpenAPI
Web interface at [http://localhost:8000/v1/ui/](http://localhost:8000/v1/ui/).

## Monitoring
All the application's log will be sent to an Elasticsearch instance. The main goal
here is to provide a real time log stream that can be monitored using Kibana.

Since this work is in the very beginning stage, I've created a separated docker
compose file. To call the application along with the future ELK stack (Logstash will
be added later), run:

```shell
$ docker-compose -f docker-compose-dev-elk.yaml up
```

Elasticsearch will be available at *http://localhost:9200* and Kibana at
*http://localhost:5601*.

## Testing
The specific ```docker-compose-test.yaml``` file was made to run unit tests with
*PyTest* and generate both test and coverage reports inside the *tests* directory:

```shell
$ docker-compose -f docker-compose-test.yaml up
```

This should start the container, run the tests, generate the reports and exit.

## Structure
Here is how the project is structured:

* **/controllers**: Responsible for handling HTTP request and response
* **/ml**: Where the machine learning models resides to be accessed by the controllers, we can think as our business layer
* **/resources**: Configuration and stand-alone scripts for tooling
* **/tests**: Unit and system tests, coverage and test reports
* **application.py**: Application setup and starting point

## References
* [Connexion](https://github.com/zalando/connexion)
* [Connexion's documentation](https://connexion.readthedocs.io)
* [OpenAPI Specification](https://swagger.io/docs/specification)
* [Swagger](https://github.com/swagger-api)
* [The Team Data Science Process lifecycle](https://docs.microsoft.com/en-us/azure/machine-learning/team-data-science-process/lifecycle)
* [The Twelve-Factor App](https://12factor.net)
