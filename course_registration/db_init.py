import sqlite3
import os

DB_FILE = "course_registration/Academia.db"


def get_db_connection():
    """Establishes a connection to the SQLite database with FK enforcement."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def initialize_database():
    """Resets the database and seeds it with the specified data."""
    # Remove existing DB to ensure a clean reset
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    # Read schema and create tables
    with open("course_registration/schema.sql", "r") as f:
        schema = f.read()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.executescript(schema)

    # Seed data (as requested)
    seed_data = [
        # Teachers
        (
            "INSERT INTO teachers (name, email) VALUES (?, ?)",
            [
                ("Dr. Grace Hopper", "grace.hopper@university.com"),
                ("Dr. Alan Turing", "alan.turing@university.com"),
                ("Prof. Donald Knuth", "donald.knuth@university.com"),
            ],
        ),
        # Students
        (
            "INSERT INTO students (name, email) VALUES (?, ?)",
            [
                ("Alice Johnson", "alice.johnson@student.com"),
                ("Bob Smith", "bob.smith@student.com"),
                ("Catherine Lee", "catherine.lee@student.com"),
                ("David Kim", "david.kim@student.com"),
            ],
        ),
        # Courses
        (
            "INSERT INTO courses (title, teacher_id) VALUES (?, ?)",
            [
                ("Introduction to Computer Science", 1),  # Grace Hopper
                ("Discrete Mathematics", 2),               # Alan Turing
                ("Algorithms and Data Structures", 3),     # Donald Knuth
            ],
        ),
        # Enrollments
        (
            "INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)",
            [
                (1, 1),  # Alice → Intro to CS
                (2, 1),  # Bob → Intro to CS
                (3, 2),  # Catherine → Discrete Math
                (4, 2),  # David → Discrete Math
                (1, 3),  # Alice → Algorithms
                (3, 3),  # Catherine → Algorithms
            ],
        ),
    ]

    for query, data in seed_data:
        cursor.executemany(query, data)

    conn.commit()
    conn.close()
    print("Database reset and seeded with the specified data.")


if __name__ == "__main__":
    initialize_database()
