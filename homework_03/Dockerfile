# docker build . -t webapp
# docker run -p 8000:8000 -d webapp

FROM python:3.9-buster

ENV PYTHONBUFFERED=1
WORKDIR /var/app
COPY ./pyproject.toml /var/app/pyproject.toml

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-ansi

COPY . /var/app

CMD ["uvicorn", "project.hw3.main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000