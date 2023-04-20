ARG POETRY_VERSION=1.4

FROM python:3.10-slim as base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=80 \
    WEB_CONCURRENCY=3
WORKDIR /dash
EXPOSE ${PORT}

FROM base as poetry
ARG POETRY_VERSION
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_IGNORE_INSTALLED=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_CACHE_DIR=/opt/.cache
# hadolint ignore=DL3013
RUN pip install --upgrade pip setuptools \
    && pip install poetry=="${POETRY_VERSION}"
RUN python -m venv /venv
COPY pyproject.toml poetry.lock* ./
# hadolint ignore=SC1091
RUN . /venv/bin/activate \
    && poetry install --only main \
    --no-root --no-interaction --no-ansi

FROM poetry as dev
# hadolint ignore=SC1091
RUN . /venv/bin/activate \
    && poetry install \
    --no-root --no-interaction --no-ansi
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
COPY . .
CMD ["flask", "--app", "app:create_app()", "run"]

FROM base as prod
COPY --from=poetry /venv /venv
ENV PATH="/venv/bin:${PATH}"
COPY . .
CMD ["gunicorn", "app:create_app()"]
