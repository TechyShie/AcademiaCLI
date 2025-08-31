from .base import BaseModel

class User(BaseModel):
    def __init__(self, name, email, id=None):
        super().__init__(id)
        self.name = name
        self.email = email
