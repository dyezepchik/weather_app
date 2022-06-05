FROM python:3.9-slim

RUN groupadd -r user1 && useradd --no-log-init --create-home -r -g user1 user1

ENV PIPENV_PIPFILE="/home/user1/Pipfile"

COPY ./Pipfile ./Pipfile.lock /home/user1/

WORKDIR /home/user1/
RUN pip3 install pipenv && \
    pipenv install --system && \
    pip3 uninstall pipenv -y

USER user1
