ARG BASE_IMAGE=pfeiffermax/uvicorn-poetry:3.2.0-python3.12.0-slim-bookworm
FROM ${BASE_IMAGE}

COPY --chown=python_application:python_application ./poetry.lock ./pyproject.toml /application_root/

RUN poetry install --no-interaction --no-root --without dev

COPY --chown=python_application:python_application /src /application_root/src/

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
