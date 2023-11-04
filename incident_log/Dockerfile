FROM python:3.8
ARG REBUILD=1111111
ENV DJANGO_SETTINGS_MODULE incident_log.settings_docker
RUN pip install --upgrade pip
WORKDIR /code
COPY . /code/
RUN ls -a
RUN pip install -r requirements.txt