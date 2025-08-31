from course_registration.db_init import initialize_database
from course_registration.services.student_service import StudentService
from course_registration.services.teacher_service import TeacherService
from course_registration.services.course_service import CourseService
from course_registration.services.registration_service import RegistrationService
from rich.console import Console
from rich.table import Table
from rich import box
from typing import List, Tuple, Optional, Callable

console = Console(force_terminal=True)

# ---------- Helpers ----------

def render_rows(title: str, cols: List[Tuple[str, str]], rows):
    if not rows:
        print("No records found.")
        return
    t = Table(title=title, box=box.SIMPLE)
    for _, header in cols:
        t.add_column(header)
    for r in rows:
        t.add_row(*[str(r[k] if r[k] is not None else "") for k, _ in cols])
    console.print(t)

def prompt_int(label: str) -> Optional[int]:
    v = input(label).strip()
    return int(v) if v.isdigit() else None

def prompt_fields(spec: List[Tuple[str, type]]):
    values = []
    for name, tp in spec:
        s = input(f"Enter {name.replace('_',' ')}: ").strip()
        if tp is int:
            if not s.isdigit():
                print(f"Invalid {name}. Must be a number.")
                return None
            values.append(int(s))
        else:
            values.append(s)
    return values

# Generic CRUD wired by naming convention on services
ENTITIES = {}

def add_entity(entity: str):
    cfg = ENTITIES[entity]
    vals = prompt_fields(cfg['fields'])
    if vals is None: return
    try:
        getattr(cfg['service'], f"add_{entity}")(*vals)
        print(f"{entity.capitalize()} added successfully!")
    except Exception as e:
        print(f"Error adding {entity}: {e}")

def list_entity(entity: str):
    cfg = ENTITIES[entity]
    try:
        rows = getattr(cfg['service'], f"get_all_{cfg['plural']}")()
        render_rows(cfg['title'], cfg['columns'], rows)
    except Exception as e:
        print(f"Error listing {cfg['plural']}: {e}")

def update_entity(entity: str):
    cfg = ENTITIES[entity]
    _id = prompt_int(f"Enter {entity} ID to update: ")
    if _id is None:
        print("Invalid ID.")
        return
    vals = prompt_fields(cfg['fields'])
    if vals is None: return
    try:
        getattr(cfg['service'], f"update_{entity}")(_id, *vals)
        print(f"{entity.capitalize()} updated successfully!")
    except Exception as e:
        print(f"Error updating {entity}: {e}")

def delete_entity(entity: str):
    cfg = ENTITIES[entity]
    _id = prompt_int(f"Enter {entity} ID to delete: ")
    if _id is None:
        print("Invalid ID.")
        return
    try:
        getattr(cfg['service'], f"delete_{entity}")(_id)
        print(f"{entity.capitalize()} deleted successfully!")
    except Exception as e:
        print(f"Error deleting {entity}: {e}")

# ---------- Enrollment flows ----------
def enroll_student():
    print("\n--- Enroll Student in Course ---")
    list_entity('student')
    list_entity('course')
    sid = prompt_int("Enter student ID: ")
    cid = prompt_int("Enter course ID: ")
    if sid is None or cid is None:
        print("Invalid IDs.")
        return
    try:
        registration_service.enroll_student(sid, cid)
        print("Enrollment successful!")
        print("Updated roster for the course:")
        _print_students_in_course(cid)
    except Exception as e:
        print(f"Error enrolling student: {e}")

def list_students_in_course():
    print("\n--- List Students in a Course ---")
    list_entity('course')
    cid = prompt_int("Enter course ID: ")
    if cid is None:
        print("Invalid course ID.")
        return
    _print_students_in_course(cid)

def _print_students_in_course(course_id: int):
    try:
        rows = registration_service.get_students_in_course(course_id)
        render_rows(f"Students in Course {course_id}", [("id","ID"),("name","Name"),("email","Email")], rows)
    except Exception as e:
        print(f"Error listing students in course: {e}")

def list_courses_for_student():
    print("\n--- List Courses for a Student ---")
    sid = prompt_int("Enter student ID: ")
    if sid is None:
        print("Invalid student ID.")
        return
    try:
        rows = registration_service.get_courses_for_student(sid)
        if not rows:
            print("This student is not enrolled in any courses.")
            return
        render_rows("Courses for Student", [("id","Course ID"),("title","Title"),("teacher_name","Teacher")], rows)
    except Exception as e:
        print(f"Error listing student's courses: {e}")

# ---------- Menus ----------

def menu(title: str, options: List[Tuple[str, str, Callable]]):
    while True:
        print(f"\n=== {title} ===")
        for key, text, _ in options:
            print(f"{key}. {text}")
        choice = input("Enter your choice: ").strip()
        for key, _, fn in options:
            if choice == key:
                if fn is None:
                    return
                fn()
                break
        else:
            print("Invalid choice. Please try again.")

def manage_entity_menu(entity: str):
    cap = entity.capitalize()
    menu(f"Manage {cap}s", [
        ("1", f"Add {cap}", lambda: add_entity(entity)),
        ("2", f"List All {cap}s", lambda: list_entity(entity)),
        ("3", f"Update {cap}", lambda: update_entity(entity)),
        ("4", f"Delete {cap}", lambda: delete_entity(entity)),
        ("5", "Back to Main Menu", None),
    ])

# ---------- Entry ----------
if __name__ == "__main__":
    initialize_database()

    student_service = StudentService()
    teacher_service = TeacherService()
    course_service = CourseService()
    registration_service = RegistrationService()

    ENTITIES = {
        'student': {
            'service': student_service,
            'plural': 'students',
            'title': 'Students',
            'fields': [('name', str), ('email', str)],
            'columns': [("id","ID"),("name","Name"),("email","Email")],
        },
        'teacher': {
            'service': teacher_service,
            'plural': 'teachers',
            'title': 'Teachers',
            'fields': [('name', str), ('email', str)],
            'columns': [("id","ID"),("name","Name"),("email","Email")],
        },
        'course': {
            'service': course_service,
            'plural': 'courses',
            'title': 'Courses',
            'fields': [('title', str), ('teacher_id', int)],
            'columns': [("id","ID"),("title","Title"),("teacher_id","Teacher ID")],
        },
    }

    menu("Welcome to AcademiaCLI", [
        ("1", "Manage Students", lambda: manage_entity_menu('student')),
        ("2", "Manage Teachers", lambda: manage_entity_menu('teacher')),
        ("3", "Manage Courses", lambda: manage_entity_menu('course')),
        ("4", "Manage Enrollments", lambda: menu("Enrollment Management", [
            ("1", "Enroll Student in Course", enroll_student),
            ("2", "List Students in a Course", list_students_in_course),
            ("3", "List Courses for a Student", list_courses_for_student),
            ("4", "Back to Main Menu", None),
        ])),
        ("0", "Exit", None),
    ])
