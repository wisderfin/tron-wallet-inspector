FROM python:3.12-slim AS migrations
WORKDIR /migrations
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# COPY settings.py .
# COPY models.py .
# COPY migrations .
# COPY .env .
# COPY alembic.ini .


# FROM python AS api
# WORKDIR /app
# COPY requirements/api.txt .
# RUN pip install --no-cache-dir -r api.txt
