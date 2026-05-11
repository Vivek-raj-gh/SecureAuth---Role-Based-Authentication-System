# 🔐 SecureAuth — Role-Based Authentication System

SecureAuth is a secure backend authentication system built using Flask, JWT, and SQLite.  
The project implements user registration, login authentication, role-based authorization, protected APIs, and interactive Swagger documentation following modern backend development practices.

---

# 🚀 Features

- ✅ User Registration & Login
- ✅ JWT Token-Based Authentication
- ✅ Role-Based Access Control (Admin/User)
- ✅ Password Hashing & Security
- ✅ Protected REST APIs
- ✅ Swagger/OpenAPI Documentation
- ✅ Interactive API Testing
- ✅ Modular Flask Architecture
- ✅ SQLite Database Integration
- ✅ Input Validation & Error Handling

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend Development |
| Flask | Web Framework |
| Flask-JWT-Extended | JWT Authentication |
| Flask-SQLAlchemy | ORM & Database Handling |
| SQLite | Database |
| Flasgger | Swagger/OpenAPI Documentation |
| Werkzeug | Password Hashing |
| Thunder Client / Postman | API Testing |
| Gunicorn | Production WSGI Server for Deployment |

---

# 📂 Project Structure

```bash
SecureAuth/
│
├── app.py
├── config.py
├── requirements.txt
│
├── models/
│   └── user_model.py
│
├── routes/
│   └── auth_routes.py
│
├── utils/
│   └── validators.py
│
└── README.md
```

---

# ⚡ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Vivek-raj-gh/SecureAuth---Role-Based-Authentication-System.git
```

---

## 2️⃣ Navigate to Project

```bash
cd SecureAuth---Role-Based-Authentication-System
```

---

## 3️⃣ Create Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Run Application

```bash
python app.py
```

Server will start at:

```bash
http://127.0.0.1:5000
```

---

# 📘 Swagger API Documentation

Swagger UI:

```bash
http://127.0.0.1:5000/apidocs
```

Features:
- Interactive API Testing
- JWT Authorization Support
- Request/Response Schemas
- API Endpoint Documentation

---

# 🔑 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/register` | POST | Register new user |
| `/login` | POST | User authentication |
| `/dashboard` | GET | Protected user dashboard |
| `/admin` | GET | Admin-only protected route |

---

# 🔐 JWT Authorization

Protected routes require JWT token.

Add token in request header:

```bash
Authorization: Bearer YOUR_TOKEN
```

---

# 📌 Example Login Request

```json
{
    "username": "vivek@gmail.com",
    "password": "Password123"
}
```

---

# 📌 Future Enhancements

- Refresh Tokens
- Email Verification
- Password Reset
- PostgreSQL Integration
- Docker Deployment
- CI/CD Pipeline
- Cloud Deployment

---

# 👨‍💻 Author

**Vivek Vardhan Saraswathi**

- GitHub: https://github.com/Vivek-raj-gh
- LinkedIn: https://www.linkedin.com/in/vivek-vardhan-saraswathi-226000270/

---

# ⭐ Project Goal

This project was developed to strengthen backend engineering concepts including authentication systems, REST API development, security implementation, API documentation, and scalable Flask application architecture.
