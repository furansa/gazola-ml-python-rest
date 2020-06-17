FROM python:3.8

WORKDIR /api

COPY ./Pipfile /api/

# TODO: Check for automated version number control
LABEL version="0.0.1" \
      description="Gazola Machine Learning REST API"

# Update the system and install required packages
RUN apt-get update && apt-get upgrade -y && apt-get clean && \
useradd -d /api -M gazola && \
pip3 install --upgrade pip && pip3 install pipenv && pipenv install --dev --skip-lock --system

# Run the application as unprivileged user
USER gazola

ENTRYPOINT ["/api/resources/entrypoint.sh"]
