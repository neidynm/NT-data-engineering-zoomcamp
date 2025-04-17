# 🚖 NYC Taxi Data Pipeline Project

This project sets up a local data pipeline using Docker, PostgreSQL, and Python to ingest NYC Yellow Taxi trip data in Parquet format into a PostgreSQL database. It includes scripts for data ingestion and batch processing.

## 🧱 Project Structure

```
.
├── ingest_data.py         # Script to ingest parquet data into PostgreSQL
├── docker-compose.yml     # Docker setup for PostgreSQL, pgAdmin, and app
├── Dockerfile             # (Expected) Docker setup for building the app
├── .env                   # Environment variables used by docker-compose
└── README.md              # You are here!
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

### 2. Set Environment Variables

Create a `.env` file in the root directory with the following content:

```env
POSTGRES_USER=root
POSTGRES_PASSWORD=root
POSTGRES_DB=ny_taxi
```

### 3. Start Services

Run the following to spin up PostgreSQL, pgAdmin, and your application container:

```bash
docker compose --env-file .env up --build -d
```

### 4. Ingest Data

Run the following command to run the ingestion script
```bash
ocker exec introduction_docker-app-1 python3 /app/ingest_data.py
```

## 🛠 Tools & Tech

- **Python**: for scripting and data ingestion
- **Docker**: for containerizing services
- **PostgreSQL**: database for storing taxi trip data
- **pgAdmin**: database administration interface
- **Pandas + PyArrow**: for processing Parquet data

## 📊 Accessing pgAdmin

After running `docker-compose`, go to [http://localhost:8080](http://localhost:8080) and log in with your credentials, the above are just an example:

- Email: `admin@admin.com`
- Password: `root`

Then add a new server with:
- Host: `pgdatabase`
- Username: `root`
- Password: `root`

## 📌 Notes

- This setup assumes you are running on a Unix-like system.
- The `Dockerfile` should exist to build the app service, even though it was not uploaded.

## 📂 License

MIT (or your license of choice)
