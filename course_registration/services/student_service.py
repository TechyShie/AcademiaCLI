from ..repositories.student_repository import StudentRepository
from ..models.student import Student

class StudentService:
    def __init__(self):
        self.student_repo = StudentRepository()

    def add_student(self, name, email):
        student = Student(name, email)
        self.student_repo.add(student)

    def get_all_students(self):
        return self.student_repo.get_all()

    def update_student(self, id, name, email):
        student = Student(name, email, id)
        self.student_repo.update(student)

    def delete_student(self, id):
        self.student_repo.delete(id)
