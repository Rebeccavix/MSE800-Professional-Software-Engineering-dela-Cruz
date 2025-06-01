'''Inheritance Practice
    Create a class 'Person' with attributes name and age, and a method 'introduces()'.
    Then create a class 'Student' that inherits from 'Person', with an extra attribute 'student_id', and override the 'introduce()' method to include the student ID.
    
    Expected Output:
    "Hi, I'm John, 20 years old, and my student ID is 1234."
    '''

# Parent Class


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old."

# Child Class (Single Inheritance)


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Initialize parent attributes
        self.student_id = student_id  # Add child-specific attribute

    def introduce(self):  # Override parent method
        return f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}."


# Create instances
person = Person("Alice", 25)
student = Student("John", 20, 1234)

# Test methods
print("Person Introduction:")
print(person.introduce())

print("\nStudent Introduction:")
print(student.introduce())

print("\nMethod Override:")
people = [person, student]
for p in people:
    print(f"• {p.introduce()}")

'''
Single Inheritance
    Linear Relationship
    Student is a Person
    Every student is a person, but not every person is a student
    Natural parent-child relationship
Inheritance
    Student inherits name and age from Person

    One child class (Student) inheriting from one parent class (Person) with method overriding to specialize behavior.
'''
