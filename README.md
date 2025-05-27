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


Copyright © 2025 alby13

All rights reserved.

This software and associated documentation files (the "Software") are provided "as is", for personal viewing and display purposes only.

You are not permitted to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS DISPLAYED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Original License: Apache License v2.0
