# Simple Student Grading System Using classes
# Task: Create students, record their grades, and show results.
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Invalid grade! Please enter a value between 0 and 100.")

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def show_results(self):
        """Displays the student's grades and average."""
        if self.grades:
            print(f"\nStudent: {self.name}")
            print(f"Grades: {self.grades}")
            print(f"Average Grade: {self.calculate_average():.2f}")
        else:
            print(f"\nStudent: {self.name} has no recorded grades.")


# Example usage
student1 = Student("Alice")
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)

student2 = Student("Bob")
student2.add_grade(92)
student2.add_grade(88)

# Show results
student1.show_results()
student2.show_results()


# Output:
# Student: Alice
# Grades: [85, 90, 78]
# Average Grade: 84.33

# Student: Bob
# Grades: [92, 88]
# Average Grade: 90.00
