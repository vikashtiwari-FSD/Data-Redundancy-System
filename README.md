# Cloud-Based Data Redundancy Removal System

## Overview

The Cloud-Based Data Redundancy Removal System is a Flask-based web application developed as part of the CodeAlpha Cloud Computing Internship.

The system validates user data before storing it, detects duplicate records, classifies false positives, and stores only unique records in the database. It also maintains submission logs and synchronizes valid records with Firebase Firestore.

---

## Features

- Duplicate Detection
- False Positive Classification
- User Data Validation
- MySQL Database Integration
- Firebase Firestore Integration
- Dashboard with Statistics
- Search Records
- Submission Logging
- Responsive Bootstrap UI

---

## Technologies Used

- Python
- Flask
- MySQL
- Firebase Firestore
- HTML
- CSS
- Bootstrap 5

---

## Project Structure

"""
Data-Redundancy-System/
app.py
config.py
database/
firebase/
routes/
static/
templates/
utils/
screenshots/
requirements.txt
README.md

"""

---

## Workflow

1. User enters details.
2. Input validation is performed.
3. Duplicate records are detected.
4. Unique records are stored in MySQL.
5. Unique records are synchronized with Firebase Firestore.
6. Every submission is logged.
7. Dashboard displays statistics.
8. Search allows viewing stored records and submission history.

---

## Installation

### Clone Repository

"""bash
git clone https://github.com/vikashtiwari-FSD/Data-Redundancy-System.git
"""

### Navigate

"""bash
cd Data-Redundancy-System
"""

### Install Packages

"""bash
pip install -r requirements.txt
"""

### Configure

Update 'config.py' with your MySQL credentials.

Place your Firebase Service Account JSON file inside:

"""
firebase/
"""

### Run

"""bash
python app.py
"""

---

## Screenshots

## Screenshots

### Home Page

![Home Page](screenshots/home_page.png)

---

### Successful Submission

![Successful Submission](screenshots/successful_submission.png)

---

### Duplicate Detection

![Duplicate Detection](screenshots/duplicate_detection.png)

---

### Search Page

![Search Page](screenshots/search_page.png)

---

### Dashboard

![Dashboard](screenshots/dashboard.png)

---

### Firebase Firestore

![Firebase Firestore](screenshots/firebase_firestore.png)

---

### MySQL Database

![MySQL Database](screenshots/mysql_database.png)

---

## Author

Vikash Tiwari

CodeAlpha Cloud Computing Internship

2026