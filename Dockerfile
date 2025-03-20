FROM python:3.13

RUN mkdir /app
RUN mkdir /app/scripts

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ARG POETRY_HOME=/etc/poetry
ENV PATH="${PATH}:${POETRY_HOME}/bin"

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python3 -

COPY ./pyproject.toml /app
RUN poetry lock
RUN poetry install --no-interaction --no-cache --no-root

COPY ./school /app
COPY ./scripts /app/scripts
RUN chmod +x ./scripts/entrypoint.sh

ENV PYTHONPATH=.

ENTRYPOINT [ "bash", "./scripts/entrypoint.sh" ]
