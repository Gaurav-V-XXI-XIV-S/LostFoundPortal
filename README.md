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

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

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

```bash
python app.py
```

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
