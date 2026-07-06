# Smart AI Lost & Found Portal

A production-style full-stack web application for reporting lost and found items, matching item photos with OpenCV, managing claims, and monitoring activity through user and admin dashboards.

## Features

- User registration, login, logout, remember-me sessions, password hashing, and forgot-password page
- Lost and found item reporting with image upload preview and validation
- OpenCV matching with ORB feature detection, BFMatcher, HSV histogram comparison, and confidence scoring
- User dashboard with report counts, charts, recent reports, profile management, and claim history
- Admin dashboard for analytics, user management, report moderation, and claim review
- Search and filtering by item name, category, location, and date
- Bootstrap 5 responsive UI with Chart.js, Font Awesome, AOS animations, and SaaS-style layouts
- MySQL schema with primary keys, foreign keys, indexes, and claim relationships
- Deployment files for Render, Railway, PythonAnywhere, and Gunicorn

## Tech Stack

- Backend: Python, Flask
- Database: MySQL
- AI/Image Processing: OpenCV, NumPy
- Frontend: HTML5, CSS3, Bootstrap 5, JavaScript, Font Awesome, Chart.js, AOS
- Auth: Flask sessions and Werkzeug password hashing

## Project Structure

```text
LostFoundPortal/
|-- app.py
|-- config.py
|-- requirements.txt
|-- database.sql
|-- Procfile
|-- runtime.txt
|-- static/
|-- templates/
|-- routes/
|-- models/
|-- utils/
|-- ai/
|-- database/
`-- tests/
```

## Local Setup

1. Create and activate a virtual environment.

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Create the MySQL database.

```bash
mysql -u root -p < database.sql
```

4. Update `.env` with your MySQL username, password, database name, and secret key.

5. Seed an admin user.

```bash
python database/seed_admin.py
```

Default admin credentials come from `.env`:

```text
ADMIN_EMAIL=admin@lostfound.local
ADMIN_PASSWORD=Admin@12345
```

6. Run the application.

```bash
python app.py
```

Open `http://127.0.0.1:5000`.

## AI Matching

The matching system lives in `ai/`:

- `image_match.py` loads, resizes, denoises, and compares HSV histograms
- `orb_match.py` extracts ORB features and matches descriptors with BFMatcher
- `similarity_engine.py` combines ORB and histogram scores into a final confidence percentage

When a user submits a lost-item report, the app compares it against open found-item reports in the same category and displays possible matches.

## Deployment Notes

### Render

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Add environment variables from `.env`
- Use a hosted MySQL provider such as Railway, PlanetScale, Aiven, or ClearDB

### Railway

- Connect the GitHub repository
- Add a MySQL service
- Copy the MySQL connection details into environment variables
- Start command: `gunicorn app:app`

### PythonAnywhere

- Create a MySQL database from the dashboard
- Upload the project or pull from GitHub
- Install requirements in a virtual environment
- Configure the WSGI file to import `app` from `app.py`
- Set environment variables in the web app configuration

## Security Checklist

- Replace `SECRET_KEY` before deployment
- Set `SESSION_COOKIE_SECURE=True` when running behind HTTPS
- Keep `.env` out of Git
- Restrict upload size and image file extensions
- Use a managed MySQL service with strong credentials

## Portfolio Talking Points

- Modular Flask architecture with blueprints, route guards, and database helper functions
- Real AI component using ORB descriptors and histogram similarity
- Complete CRUD flow for reports and admin moderation
- Responsive dashboards with visual analytics
- Deployment-ready configuration and schema-first database design
