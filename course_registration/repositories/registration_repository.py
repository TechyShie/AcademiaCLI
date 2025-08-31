from .base_repository import BaseRepository
from ..models.registration import Registration

class RegistrationRepository(BaseRepository):
    def __init__(self):
        super().__init__("enrollments")

    def add(self, registration):
        query = f"INSERT INTO {self.table_name} (student_id, course_id) VALUES (?, ?)"
        self._execute(query, (registration.student_id, registration.course_id))

    def get_by_student_and_course(self, student_id, course_id):
        query = f"SELECT * FROM {self.table_name} WHERE student_id = ? AND course_id = ?"
        return self._execute(query, (student_id, course_id), fetch="one")

    def get_students_by_course(self, course_id):
        query = f"""
            SELECT s.id, s.name, s.email 
            FROM students s
            JOIN {self.table_name} e ON s.id = e.student_id
            WHERE e.course_id = ?
        """
        return self._execute(query, (course_id,), fetch="all")

    def get_courses_by_student(self, student_id):
        query = f"""
            SELECT c.id, c.title, t.name as teacher_name
            FROM courses c
            JOIN {self.table_name} e ON c.id = e.course_id
            LEFT JOIN teachers t ON c.teacher_id = t.id
            WHERE e.student_id = ?
        """
        return self._execute(query, (student_id,), fetch="all")
