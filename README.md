# 📘 Academic CLI - Course Registration System  

## 📖 Project Overview  
The **Academic CLI System** is a command-line tool designed to manage a simple academic database. It allows **students, teachers, and courses** to be added, retrieved, and linked together through enrollments. Built with **Python** and **SQLite**, the project demonstrates database design, SQL queries, and Python-based data management in a structured way.  

---

### 📽️ Video Presentation  
[Watch the Demo Here](https://your-video-link.com)  

---

## 🎯 Problem Statement  
Academic institutions need a way to keep track of **students, teachers, courses, and enrollments**. Without a proper system, managing these relationships manually is error-prone and inefficient.  

---

## 💡 Solution  
This CLI provides a **lightweight and user-friendly solution** to manage an academic environment. It ensures:  
- Clean database schema design.  
- Organized student–course–teacher relationships.  
- Simple operations like **add, list, delete, enroll, and view**.  
- A foundation for scaling into a larger system.  

---

## ✨ Features  
- **Students Management** → Add, list, search, and delete students.  
- **Teachers Management** → Add and view teachers.  
- **Courses Management** → Add and view courses (linked to teachers).  
- **Enrollments** → Link students to courses.  
- **Relational Queries** → View courses by student, students by course, etc.  
- **Pretty Tables** → Integrated with the [Rich](https://github.com/Textualize/rich) library for visually appealing outputs.  

---

## 🗂️ Project Structure  
```
course_registration/
│── models/
│   ├── base.py          # BaseModel (common fields/logic)
│   ├── user.py          # User model
│   ├── student.py       # Student model
│   ├── teacher.py       # Teacher model
│   ├── course.py        # Course model
│   └── registration.py  # Registration (student <-> course)
│
│── repositories/
│   ├── base_repository.py       # Generic CRUD operations
│   ├── user_repository.py       # CRUD for users
│   ├── student_repository.py    # CRUD for students
│   ├── teacher_repository.py    # CRUD for teachers
│   ├── course_repository.py     # CRUD for courses
│   └── registration_repository.py  # CRUD for registrations
│
│── services/
│   ├── auth_service.py          # Login / signup logic
│   ├── student_service.py       # Student actions (register course, view courses)
│   ├── teacher_service.py       # Teacher actions (create course, view students)
│   └── course_service.py        # Course actions (list, search, etc.)
│
│── schema.sql       # Database schema (tables)
│── db_init.py       # Script to initialize DB with schema.sql
│── main.py          # Entry point for the CLI
```
## 🔗 Database Relationships  

- **One Teacher → Many Courses**  
- **One Student → Many Courses** 
- **One Course → Many Students** 


---

## 👩‍💻 Author  

Developed by **Susan Wanjiru** ✨  

---

## 📜 License  

This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it.  

```text
MIT License

Copyright (c) 2025 Susan Wanjiru
