

---

# 🧠 **AllocEngine** – Smart Exam Hall Allocation System

**AllocEngine** is a **Django-based intelligent exam hall allocation system** developed for **Kamaraj College of Engineering and Technology (KCET)**. It automates the assignment of students to exam halls and seats with built-in support for QR verification, real-time allocation tracking, and seamless admin control.

---

## 📌 Table of Contents

* [Project Overview](#project-overview)
* [Key Features](#key-features)
* [System Architecture](#system-architecture)
* [Working Process](#working-process)
* [Tech Stack](#tech-stack)
* [Installation Guide](#installation-guide)
* [Future Scope](#future-scope)
* [Screenshots](#screenshots)
* [Contributors](#contributors)
* [License](#license)

---

## 🚀 Project Overview

**AllocEngine** is built to **eliminate manual errors**, **save administrative time**, and ensure **fair and systematic** exam hall assignments. With a responsive UI for students and a powerful admin backend, the system streamlines all critical operations from student mapping to exam-day validation using **QR code technology**.

---

## 🌟 Key Features

✅ **Automated Hall & Seat Allocation**
✅ **QR Code Generation & Scanning for Authentication**
✅ **Real-time Dashboard for Admin Monitoring**
✅ **Exportable Reports (Excel/PDF)**
✅ **Smart Buffer Seating for Social Distancing**
✅ **Support for Special Needs Accommodation**
✅ **Multi-Exam Support with Date and Slot Configuration**
✅ **Searchable Student Record Lookup**
✅ **Mobile-Friendly Student Portal**
✅ **User Roles & Authentication System**

---

## 🧱 System Architecture

```
            ┌────────────────────────────┐
            │      Admin Interface      │
            └────────────┬──────────────┘
                         │
      ┌──────────────────▼──────────────────┐
      │      Django Backend (AllocEngine)   │
      ├──────────────┬──────────────────────┤
      │ Models       │ Views & Forms        │
      │ Allocations  │ QR Code Generator    │
      │ Users, Halls │ PDF/Excel Exports    │
      └──────────────┴──────────────────────┘
                         │
                ┌────────▼────────┐
                │    SQLite DB    │
                └─────────────────┘
                         │
                ┌────────▼────────┐
                │  Student Portal │
                └─────────────────┘
```

---

## ⚙️ Working Process

### 🧑‍💼 Admin Flow:

1. **Login to Admin Panel**
2. **Create/Edit Exams and Halls**
3. **Select Exam, Date, and Time**
4. **Bulk Upload or Manually Add Students**
5. **System Auto-Allocates Students to Seats**
6. **Generate QR-Coded Allocation Slips**
7. **Export as Excel/PDF for Invigilators**

### 👨‍🎓 Student Flow:

1. Visit the **Student Allocation Portal**
2. Enter **Roll Number**, **Year**, and **Semester**
3. View:

   * Exam Date & Time
   * Hall & Seat Number
   * Subject Name
   * QR Code
4. **Print or Save** Allocation Slip

### 🛡️ Exam-Day Verification:

* Staff scans QR Code using a mobile or scanner.
* System validates seat, subject, and roll number.
* Entry granted or flagged.

---

## 🛠️ Tech Stack

| Component          | Technology               |
| ------------------ | ------------------------ |
| Backend            | Python, Django           |
| Frontend           | HTML5, CSS3, JS          |
| Database           | SQLite (configurable)    |
| QR Generation      | `qrcode` Python module   |
| PDF Export         | `reportlab`, `xhtml2pdf` |
| Hosting (Optional) | Heroku, PythonAnywhere   |

---

## 🧪 Installation Guide

```bash
# Clone the repo
git clone https://github.com/yourusername/allocengine.git
cd allocengine

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Migrate database and create superuser
python manage.py migrate
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

---

## 🔮 Future Scope

* 📱 **Android/iOS App for Students**
* 🧾 **AI-Powered Seat Optimization**
* 🏷️ **Printable Hall Labels and ID Verification**
* 💬 **Email/SMS Notifications for Students**
* 🧠 **ML-based Student Arrangement (e.g., prevent groupings)**
* 🔒 **Role-Based Admin Permissions (Clerk, Super Admin)**

---

## 📸 Screenshots *(Optional Section)*
![Image](https://github.com/user-attachments/assets/e26ecfee-8c14-46e8-a460-9268341548ab)
![Image](https://github.com/user-attachments/assets/d0285fff-99a3-44d8-9c5b-226844676804)
![Image](https://github.com/user-attachments/assets/6998b0cd-1185-4500-b5bd-ac6f266f5e91)
![Image](https://github.com/user-attachments/assets/1c780482-db08-4c12-82f3-c607f6bd6765)
<!-- Failed to upload "projecy.mp4" -->
![Image](https://github.com/user-attachments/assets/613786b8-2c26-42a7-8f66-b2694fffddb6)
![Image](https://github.com/user-attachments/assets/7e158486-ff80-4286-b47e-101e986d13da)
![Image](https://github.com/user-attachments/assets/07a170cb-e764-40bb-a664-621554a20407)

You can insert screenshots using:

```markdown
![Dashboard](screenshots/dashboard.png)
![QR Verification](screenshots/qr_scan.png)
```

---

## 👨‍💻 Contributors

* **KCET Mini Project Team – 2025**
* Guided by: \[Professor’s Name]

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE.md` for more information.

---

Would you like me to export this entire content as a `.md` file or zip folder with starter Django project structure and this README?
