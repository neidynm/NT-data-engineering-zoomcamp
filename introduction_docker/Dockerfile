# This sets the base image for the Docker container to the official Python 3.10 image from Docker Hub.
FROM python:3.10

# Updates the list of available packages and installs 'wget' (the '-y' is used to auto-confirm install).
RUN apt-get update && apt-get install -y wget

# Updates the package list again and installs the PostgreSQL client (useful for interacting with PostgreSQL databases from the container).
RUN apt-get update && apt-get install -y postgresql-client

# Sets the working directory in the container to '/app'. All subsequent commands will be run from this directory.
WORKDIR /app

# Copies the 'requirements.txt' file from your local machine into the container's '/app' directory.
COPY requirements.txt requirements.txt

# Installs the Python packages listed in 'requirements.txt' using pip. '--no-cache-dir' prevents caching, keeping the image smaller.
RUN pip install --no-cache-dir -r requirements.txt

# Copies the 'ingest_data.py' script from your local machine into the container's '/app' directory.
COPY ingest_data.py ingest_data.py

# Create a directory for logs
RUN mkdir logs

# This keeps the container running indefinitely by tailing an empty file. It effectively does nothing but prevent the container from exiting.
# Use this when testing 
# CMD ["tail", "-f", "/dev/null"]

#command to run the ingest_data.py
CMD ["python3", "/app/ingest_data.py"]