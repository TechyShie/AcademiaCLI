from ..repositories.course_repository import CourseRepository
from ..models.course import Course

class CourseService:
    def __init__(self):
        self.course_repo = CourseRepository()

    def add_course(self, title, teacher_id):
        course = Course(title, teacher_id)
        self.course_repo.add(course)

    def get_all_courses(self):
        return self.course_repo.get_all()

    def update_course(self, id, title, teacher_id):
        course = Course(title, teacher_id, id)
        self.course_repo.update(course)

    def delete_course(self, id):
        self.course_repo.delete(id)
