class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []  # List to store grades

    def add_grade(self, grade):
        """Adds a grade to the student's record."""
        if 0 <= grade <= 100:  # Ensures valid grade range
            self.grades.append(grade)
        else:
            print("Invalid grade! Please enter a value between 0 and 100.")

    def calculate_average(self):
        """Calculates the average grade."""
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def show_results(self):
        """Displays the student's grades and average."""
        if self.grades:
            print(f"\nStudent: {self.name}")
            print(f"Grades: {self.grades}")
            print(f"Average Grade: {self.calculate_average():.2f}")
            print(2**5)
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
