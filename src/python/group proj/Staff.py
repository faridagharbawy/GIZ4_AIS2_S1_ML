"""
this is the Staff class that inherits from the Person class
this class is responsible for managing the employees in the hospital

it has the following attributes:
- name: the name of the staff member (inherited from Person)
- age: the age of the staff member (inherited from Person)
- position: the job title or role of the staff member
"""

class Staff(Person):
    # this is the constructor method for the Staff class
    def __init__(self, name: str, age: int, position: str):
        # calling the parent constructor to initialize name and age
        super().__init__(name, age)
        self.position = position

    # this method returns a string of the staff member's information
    # it overrides the view_info method from the Person class
    def view_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"