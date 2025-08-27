# AcademiaCLI
Academic registration in the terminal.
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
