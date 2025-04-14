FROM python:3.13-alpine AS migrations
WORKDIR /migrations
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.13-alpine AS api
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
COPY settings.py ./app
COPY .env .


FROM python:3.13-alpine AS test
WORKDIR /test
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app .
COPY settings.py .
COPY .env .
COPY tests .
CMD ["pytest", "--tb=short", "-q"]
