<<<<<<< HEAD
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
=======
# 🔍 Lost and Found Portal with AI Matching

An AI-powered Lost and Found Portal built using **Flask, Python, MySQL, and OpenCV** that helps users report lost and found items while automatically identifying potential matches using image feature extraction and text similarity techniques. The application provides a secure platform for users to submit reports, upload images, browse reported items, and recover belongings through an intelligent matching system.

---

## 📌 Overview

The Lost and Found Portal is designed to simplify the process of reporting and recovering misplaced belongings. Users can create an account, securely log in, and report either lost or found items with detailed descriptions and images. The system uses AI-powered matching to compare newly reported items with existing reports based on both textual information and uploaded images.

The portal also includes an administrator dashboard to manage users, reports, claims, and system activities. By combining computer vision with text similarity analysis, the application improves the chances of finding the rightful owner quickly and efficiently.

---

## ✨ Features

- 👤 User Registration and Login
- 🔐 Secure Authentication
- 📦 Report Lost Items
- 📦 Report Found Items
- 🤖 AI-Based Item Matching
- 🖼️ Image Similarity Detection using OpenCV ORB
- 📝 Text Similarity Matching
- 📋 Personalized User Dashboard
- 👨‍💼 Admin Dashboard
- 📊 Manage Reports and Claims
- 🔍 Search Lost and Found Items
- 📸 Image Upload Support
- 📱 Responsive User Interface

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Jinja2 Templates

### Backend
- Python
- Flask

### Database
- MySQL

### AI & Image Processing
- OpenCV
- ORB Feature Matching
- Text Similarity Engine

### Tools
- Git
- GitHub
- VS Code
- MySQL Workbench

---

## 📂 Project Structure

```text
LostFoundPortal/
│
├── ai/
│   ├── image_match.py
│   ├── orb_match.py
│   └── similarity_engine.py
│
├── database/
│   └── seed_admin.py
│
├── models/
│
├── routes/
│   ├── auth.py
│   ├── public.py
│   ├── user.py
│   └── admin.py
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── uploads/
│
├── templates/
│
├── utils/
│
├── tests/
│
├── app.py
├── config.py
├── database.sql
├── requirements.txt
├── runtime.txt
├── Procfile
└── README.md
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/LostFoundPortal.git
cd LostFoundPortal
```

### Create Virtual Environment

#### Windows
>>>>>>> d1697c59491c98976afb86d4761d6e3d8ad3d532

```bash
python -m venv .venv
.venv\Scripts\activate
```

<<<<<<< HEAD
2. Install dependencies.
=======
#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies
>>>>>>> d1697c59491c98976afb86d4761d6e3d8ad3d532

```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
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
=======
---

## 🗄️ Database Setup

### Create Database

```sql
CREATE DATABASE lost_found_portal;
```

### Import SQL File

Import the provided **database.sql** file into MySQL.

### Configure Environment Variables

Create or update the `.env` file.

```env
SECRET_KEY=your-secret-key

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your-password
MYSQL_DATABASE=lost_found_portal

ADMIN_EMAIL=admin@lostfound.local
ADMIN_PASSWORD=Admin@12345

SESSION_COOKIE_SECURE=False
```

---

## ▶️ Running the Application
>>>>>>> d1697c59491c98976afb86d4761d6e3d8ad3d532

```bash
python app.py
```

<<<<<<< HEAD
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
=======
Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🤖 AI Matching Workflow

```
User Reports Lost Item
          │
          ▼
Store Item Details
          │
          ▼
User Reports Found Item
          │
          ▼
AI Similarity Engine
          │
          ├── Image Feature Matching (OpenCV ORB)
          ├── Text Similarity
          ├── Category Matching
          ├── Color Matching
          └── Description Analysis
          │
          ▼
Generate Similarity Score
          │
          ▼
Potential Match Displayed
          │
          ▼
Admin Verification
          │
          ▼
Item Returned to Owner
```

---

## 🔐 User Roles

### User

- Register Account
- Login
- Report Lost Items
- Report Found Items
- Upload Images
- Search Items
- View Matches
- Manage Profile

### Admin

- Manage Users
- Review Reports
- Verify Claims
- Monitor System
- Manage Matches

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Login
- Register
- Dashboard
- Report Lost Item
- Report Found Item
- AI Matching Results
- Admin Dashboard

---

## 🌟 Future Enhancements

- Email Notifications
- OTP Verification
- Google Maps Integration
- QR Code-Based Item Identification
- Mobile Application
- Deep Learning Image Recognition
- Real-Time Notifications
- Chat Between Owner and Finder
- Multi-Language Support

---

## 👨‍💻 Author

**Gaurav Shelke**

MCA Student | Full Stack Developer | Python & Java Developer

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://linkedin.com/in/YOUR_PROFILE

---

## 📄 License

This project is developed for educational and learning purposes. You are free to use and modify it for personal or academic use.

---

## ⭐ If you found this project useful, don't forget to give it a Star!
>>>>>>> d1697c59491c98976afb86d4761d6e3d8ad3d532
