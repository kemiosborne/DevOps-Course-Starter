FROM python:3.10.12 AS base
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/bin/
COPY . /app
WORKDIR /app
RUN poetry install
ENTRYPOINT poetry run flask run --host 0.0.0.0

FROM base as production
ENV FLASK_DEBUG=false

FROM base as development
ENV FLASK_DEBUG=true


FROM base as test

ENTRYPOINT poetry run pytest