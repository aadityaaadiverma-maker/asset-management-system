# 🏫 Asset Management System

> A secure, Python and MySQL-based Asset Management System designed to simplify inventory management through role-based authentication and department-wise asset tracking.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)
![PyMySQL](https://img.shields.io/badge/PyMySQL-Connector-success?style=for-the-badge)
![bcrypt](https://img.shields.io/badge/bcrypt-Secure%20Authentication-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

---

## 📖 Overview

Managing assets across different departments can quickly become inefficient when records are maintained manually. This project provides a centralized solution for managing institutional assets through a secure authentication system and a relational MySQL database.

Developed using **Python** and **MySQL**, the application enables users to securely log in, manage inventory records, and perform essential database operations while maintaining department-wise organization.

---

## 🎯 Objectives

- Simplify asset inventory management
- Provide secure user authentication
- Organize assets department-wise
- Reduce manual record management
- Demonstrate practical implementation of Python and MySQL

---

## ✨ Features

### 🔐 Secure Authentication
- Password hashing using **bcrypt**
- Admin Login
- Developer Login
- User Login

### 📦 Asset Management
- Add new assets
- View available assets
- Update existing asset details
- Delete assets
- Search and retrieve records

### 🗂 Department-wise Organization
Assets are maintained separately for different departments, allowing structured inventory management.

### 🗄 Database Automation
The application automatically creates:

- Database
- Required Tables
- User System

during the first execution.

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Application Development |
| MySQL | Relational Database |
| PyMySQL | Database Connectivity |
| bcrypt | Password Hashing & Security |

---

## 📂 Project Structure

```
asset-management-system/
│
├── main.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/aadityaaadiverma-maker/asset-management-system.git
```

### 2. Navigate to the Project

```bash
cd asset-management-system
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Ensure that:

- MySQL Server is installed
- The server is running
- Your MySQL username and password in the project configuration are correct

### 5. Run the Application

```bash
python main.py
```

On the first run, the application automatically initializes the required database and tables.

---

## 🚀 How It Works

```
Launch Application
        │
        ▼
 Secure Login
        │
        ▼
Choose User Role
        │
        ▼
Select Department
        │
        ▼
Manage Assets
(Add • View • Update • Delete)
        │
        ▼
Store & Retrieve Data
from MySQL Database
```

---

## 🔒 Security

The project follows secure authentication practices by hashing user passwords using **bcrypt** before storing them in the database.

Passwords are **never stored in plain text**, improving user credential security.

---

## 💡 Skills Demonstrated

- Python Programming
- Object-Oriented Programming Concepts
- SQL
- MySQL Database Management
- CRUD Operations
- Database Design
- Authentication Systems
- Password Hashing
- Backend Logic
- Problem Solving

---
## 📸 Screenshots

![Login Screen](screenshots/picture1.png)

---

![Main Menu](screenshots/picture2.png)

---


![Add Asset](screenshots/picture3.png)

---


![View Assets](screenshots/picture4.png)


---


![Delete Asset](screenshots/delete_asset.png)
---

## 🔮 Future Improvements

Planned enhancements include:

- Desktop GUI using Tkinter or CustomTkinter
- Web-based version using Flask or FastAPI
- QR/Barcode-based Asset Tracking
- Report Generation (PDF & Excel)
- Dashboard with Analytics
- Email Notifications
- Role-based Permission Management
- Asset Search Filters
- REST API Integration
- Cloud Database Support

---

## 📚 Learning Outcomes

This project strengthened my understanding of:

- Python Programming
- Database Design
- SQL Queries
- Authentication Systems
- Software Development Workflow
- Backend Development
- Relational Databases

---

## 👨‍💻 Authors

**Aaditya Verma**

- GitHub: https://github.com/aadityaaadiverma-maker
- LinkedIn: https://www.linkedin.com/in/aaditya-verma-ba75681b7

**Pranav Gupta**

- LinkedIn: https://www.linkedin.com/in/pranav-gupta-722b54379

## 📄 License

This project is intended for educational and learning purposes.

---

⭐ If you found this project helpful, consider giving it a star!
