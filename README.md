# Gazola Machine Learning REST API
This RESTful Web service provides endpoints to access a Machine Learning model
trained to predict apartment's prices in São Paulo state, based on some features
like total area.

The model was trained using Gazola's dataset that can be accessed [here](),
and this is an academic project as part of my post graduation course in
Artificial Intelligence and Machine Learning.

Along with the prediction endpoint it's also available a specific endpoint for
the model documentation and a Swagger interface as well.

The system is deployed using Docker to make it self-contained and allow
scalability across multiple environments.

## Running inside Docker
To build and run the application, clone the repository and run in a terminal
from the same directory where the ```docker-compose.yml``` file is:

```shell
$ docker-compose up
```
To stop the application, run from the same directory:

```
$ docker-compose stop
```

## Submiting code