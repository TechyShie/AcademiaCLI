from .base_repository import BaseRepository
from ..models.student import Student

class StudentRepository(BaseRepository):
    def __init__(self):
        super().__init__("students")

    def add(self, student):
        query = f"INSERT INTO {self.table_name} (name, email) VALUES (?, ?)"
        self._execute(query, (student.name, student.email))

    def update(self, student):
        query = f"UPDATE {self.table_name} SET name = ?, email = ? WHERE id = ?"
        self._execute(query, (student.name, student.email, student.id))
