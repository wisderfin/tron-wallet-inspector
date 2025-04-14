FROM python:3.13-alpine AS migrations
WORKDIR /migrations
COPY requirements/migration.txt .
RUN pip install --no-cache-dir -r migration.txt


FROM python:3.13-alpine AS api
WORKDIR /app
COPY requirements/api.txt .
RUN pip install --no-cache-dir -r api.txt
COPY app ./app
COPY settings.py ./app
COPY .env .


FROM python:3.13-alpine AS test
WORKDIR /test
COPY requirements/test.txt .
RUN pip install --no-cache-dir -r test.txt

COPY app .
COPY settings.py .
COPY .env .
COPY tests .
CMD ["pytest", "--tb=short", "-q"]
