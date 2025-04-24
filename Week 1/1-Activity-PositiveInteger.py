#2- Activity : You are given the test scores of 5 students across 3 subjects in a 2D NumPy array. Each row represents a student, and each column a subject.
# See below:
# scores = np.array([
#    [78, 85, 90],
#    [88, 79, 92],
#    [84, 76, 88],
#    [90, 93, 94],
#    [75, 80, 70]
#    ])  
#Tasks:
#   1. Calculate and print the average score for each student.
#   2. Calculate and print the average score for each subject.
#   3. Identify the student (row index) with the highest total score.
#   4. Add 5 bonus points to the third subject for all students.
 
import numpy as np

# Given scores array
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

# Task 1: Calculate and print the average score for each student
student_averages = np.mean(scores, axis=1)
print("Average score for each student:", student_averages)

# Task 2: Calculate and print the average score for each subject
subject_averages = np.mean(scores, axis=0)
print("Average score for each subject:", subject_averages)

# Task 3: Identify the student (row index) with the highest total score
total_scores = np.sum(scores, axis=1)
highest_score_student = np.argmax(total_scores)
print("Student with the highest total score (row index):", highest_score_student)

# Task 4: Add 5 bonus points to the third subject for all students
scores[:, 2] += 5
print("Updated scores after adding bonus points:\n", scores)

#Output: Average score for each student:
#           [84.33333333 86.33333333 82.66666667 92.33333333 75.        ]
#        Average score for each subject:
#           [83.  82.6 86.8]
#        Student with the highest total score (row index): 3
#        Updated scores after adding 5 bonus points to the third subject:
#           [[ 78  85  95]
#            [ 88  79  97]
#            [ 84  76  93]
#            [ 90  93  99]
#            [ 75  80  75]]