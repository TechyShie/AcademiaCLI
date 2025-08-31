from .base_repository import BaseRepository
from ..models.course import Course

class CourseRepository(BaseRepository):
    def __init__(self):
        super().__init__("courses")

    def add(self, course):
        query = f"INSERT INTO {self.table_name} (title, teacher_id) VALUES (?, ?)"
        self._execute(query, (course.title, course.teacher_id))

    def update(self, course):
        query = f"UPDATE {self.table_name} SET title = ?, teacher_id = ? WHERE id = ?"
        self._execute(query, (course.title, course.teacher_id, course.id))
