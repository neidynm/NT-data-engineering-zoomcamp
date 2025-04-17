FROM python:3.10

RUN apt-get update && apt-get install wget

RUN apt-get update && apt-get install -y postgresql-client

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ingest_data.py /app/ingest_data.py

CMD ["tail", "-f", "/dev/null"]