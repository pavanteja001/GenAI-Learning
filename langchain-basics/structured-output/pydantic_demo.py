from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = "pawan"
    age:Optional[int] = None #    Value can be present OR None
    email: EmailStr
    cgpa : float = Field(gt=0, lt=10, default=5, description = 'A decimal value representing the cgpa of the student')
#* Field → Used to add rules (like min/max values)

new_student = {"name":"pawan", "email" : "abc@g.com"}

student = Student(**new_student)
#. "**"" means:“Unpack dictionary into keyword arguments” -> Student(name="pawan", email="abc@g.com")


print(type(student))