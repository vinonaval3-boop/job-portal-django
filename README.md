# 🚀 Job Portal (Django Full-Stack Project)

A full-stack job portal web application developed using Python (Django) for backend 
and HTML, CSS, and JavaScript for frontend. This project simulates a real-world job 
platform where users can browse and apply for jobs, while admins manage listings and applications.

---

## 🔥 Features

- 🔐 User Authentication (Register / Login / Logout)
- 📄 Job Listing with dynamic UI
- 🔍 Real-time Job Search (JavaScript filtering)
- 📌 Detailed Job View
- 📨 Job Application with Resume Upload
- 📊 User Dashboard to track applied jobs
- 🧑‍💼 Admin Panel for job & applicant management
- 🧩 OOP Architecture with Role-based User Classes

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS (Bootstrap)
- **JavaScript:** DOM manipulation, search filtering
- **Database:** SQLite

---

## 💡 Key Highlights

- Implemented full CRUD operations using Django ORM
- Integrated file upload system (Resume handling)
- Built authentication system using Django Auth
- Designed responsive UI with Bootstrap
- Applied real-world MVC architecture
- 🧩 Implemented OOP principles: Inheritance, Encapsulation, Polymorphism via role-based user system (JobSeeker, Employer, Admin)

---

## 🧩 OOP Design — User Role System

This project includes a dedicated OOP module (`oop_demo/user_roles.py`) demonstrating core Object-Oriented Programming concepts:

| Concept | Implementation |
|---|---|
| **Class** | `User`, `JobSeeker`, `Employer`, `Admin` |
| **Inheritance** | `JobSeeker`, `Employer`, `Admin` extend `User` |
| **Encapsulation** | Private `__email`, `__password` with getter methods |
| **Polymorphism** | `login()` method behaves differently per role |

```python
# Example
seeker = JobSeeker("Vino", "vino@mail.com", "pass123", ["Python", "Django"])
employer = Employer("Ravi", "ravi@corp.com", "pass456", "Mediamint")

print(seeker.login())     # JobSeeker Vino logged in.
print(employer.login())   # Employer Ravi (Mediamint) logged in.
```

---

## ⚙️ Installation

```bash
git clone https://github.com/vinonaval3-boop/job-portal-django.git
cd job-portal-django
pip install -r requirements.txt
python manage.py runserver
```

---

## 📸 Screens

- Job Listing Page
- Job Detail Page
- Application Form
- User Dashboard
- Admin Panel

## 📦 Sample Data (Fixtures)

Pre-loaded job data available for quick setup:

```bash
python manage.py loaddata fixtures/jobs.json
```

Loads sample jobs from: TCS, Infosys, Wipro, Zoho, HCL
