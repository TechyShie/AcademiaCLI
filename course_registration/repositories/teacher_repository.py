from .base_repository import BaseRepository
from ..models.teacher import Teacher

class TeacherRepository(BaseRepository):
    def __init__(self):
        super().__init__("teachers")

    def add(self, teacher):
        query = f"INSERT INTO {self.table_name} (name, email) VALUES (?, ?)"
        self._execute(query, (teacher.name, teacher.email))

    def update(self, teacher):
        query = f"UPDATE {self.table_name} SET name = ?, email = ? WHERE id = ?"
        self._execute(query, (teacher.name, teacher.email, teacher.id))
