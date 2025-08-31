from .base import BaseModel

class Registration(BaseModel):
    def __init__(self, student_id, course_id, id=None):
        super().__init__(id)
        self.student_id = student_id
        self.course_id = course_id
