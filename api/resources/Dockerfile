FROM python:3.8

WORKDIR /api

COPY ./Pipfile /api/

LABEL description="Gazola Machine Learning REST API"

# Update the system and install required packages
ARG PIP_OPTIONS
RUN apt-get update && apt-get upgrade -y && apt-get clean && \
useradd -d /api -M gazola && \
pip3 install --upgrade pip && pip3 install pipenv && pipenv install ${PIP_OPTIONS}

# Run the application as unprivileged user
USER gazola

ENTRYPOINT ["/api/resources/entrypoint.sh"]
