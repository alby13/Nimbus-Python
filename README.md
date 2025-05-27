# Nimbus Cloud Storage (Python Flask Version)

A better cloud storage solution implemented in Python Flask.

## Quickstart

### 1. Clone the Repository

```bash
git clone https://github.com/[username]/nimbus-flask.git
cd nimbus-flask
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up Postgres with Docker

We use Docker to run a PostgreSQL database for local development:

```bash
docker run --name nimbus-db \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_DB=nimbus \
  -p 5432:5432 \
  -d postgres:latest
```

### 4. Environment Setup

Copy the `.env.example` file to `.env`:
```bash
cp .env.example .env
```

Fill in these values in your `.env` file:
```
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
BETTER_AUTH_SECRET=your_generated_secret  # Generate with: openssl rand -base64 32
```

### 5. Initialize Database

```bash
flask db init
flask db migrate
flask db upgrade
```

### 6. Start the Development Server

```bash
flask run
```

The application will be running at [http://localhost:5000](http://localhost:5000)

## Features

- Google OAuth Authentication
- File Upload and Storage
- User Dashboard
- PostgreSQL Database
- Responsive UI with Tailwind CSS
