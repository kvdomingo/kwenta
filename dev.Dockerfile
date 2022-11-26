FROM python:3.10-bullseye as base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONHASHSEED random
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PIP_DEFAULT_TIMEOUT 100
ENV POETRY_VERSION 1.2.2

FROM base as dev

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /tmp

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

WORKDIR /backend

ENTRYPOINT [ "/bin/sh", "-c", \
             "python manage.py migrate && \
             exec gunicorn kwenta.wsgi --bind 0.0.0.0:5000 --config gunicorn.conf.py --pid /tmp/gunicorn.pid --reload" ]
