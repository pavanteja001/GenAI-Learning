from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {'name':'pavan', 'age':'3f3f'}
print(new_person)
