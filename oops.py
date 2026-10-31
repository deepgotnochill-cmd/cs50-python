from abc import ABC, abstractmethod


# Abstraction: every college member must provide a role.
class CollegeMember(ABC):
    college = "DDUC"  # Class attribute shared by all members

    def __init__(self, name):
        self.name = name  # Instance attribute

    @abstractmethod
    def role(self):
        pass

    def introduce(self):
        # Calls role() on the current object.
        return f"I'm {self.name}, a {self.role()} at {self.college}."


# Inheritance: Student and Teacher extend CollegeMember.
class Student(CollegeMember):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    # Encapsulation: keep marks private and validate changes.
    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Marks must be between 0 and 100.")
        self.__marks = value

    def role(self):
        return "student"

    def study(self):
        return f"{self.name} is studying."


class Teacher(CollegeMember):
    def role(self):
        return "teacher"


# Objects: create instances from the classes.
members = [
    Student("Aditi", 92),
    Teacher("Tanaka"),
]

# Polymorphism: the same method call gives role-specific results.
for member in members:
    print(member.introduce())

student = members[0]
print(student.study())
print(f"Marks: {student.marks}")