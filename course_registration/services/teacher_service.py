from ..repositories.teacher_repository import TeacherRepository
from ..models.teacher import Teacher

class TeacherService:
    def __init__(self):
        self.teacher_repo = TeacherRepository()

    def add_teacher(self, name, email):
        teacher = Teacher(name, email)
        self.teacher_repo.add(teacher)

    def get_all_teachers(self):
        return self.teacher_repo.get_all()

    def update_teacher(self, id, name, email):
        teacher = Teacher(name, email, id)
        self.teacher_repo.update(teacher)

    def delete_teacher(self, id):
        self.teacher_repo.delete(id)
