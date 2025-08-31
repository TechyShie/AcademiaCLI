from .base import BaseModel

class Course(BaseModel):
    def __init__(self, title, teacher_id, id=None):
        super().__init__(id)
        self.title = title
        self.teacher_id = teacher_id
