from .base import BaseModel

class Student(BaseModel):
    def __init__(self, name, email, id=None):
        super().__init__(id)
        self.name = name
        self.email = email
