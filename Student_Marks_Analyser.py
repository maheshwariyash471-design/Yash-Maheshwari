import matplotlib.pyplot as plt

# Student information
name = input("Enter student name: ")

subjects = ["Python", "Maths", "DSA", "Oops", "English"]
marks = []

# Taking marks as input
for subject in subjects:
    mark = float(input(f"Enter marks in {subject}: "))
    marks.append(mark)

# Calculations
total = sum(marks)
percentage = total / len(marks)

# Grade calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Highest and lowest marks
highest = max(marks)
lowest = min(marks)

highest_subject = subjects[marks.index(highest)]
lowest_subject = subjects[marks.index(lowest)]

# Pass / Fail
status = "PASS" if percentage >= 40 else "FAIL"

# Display result
print("\n========== STUDENT RESULT ==========")
print("Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Highest:", highest_subject, "-", highest)
print("Lowest:", lowest_subject, "-", lowest)
print("Status:", status)

# Create graph
plt.bar(subjects, marks)

plt.title("Student Marks Analysis")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.ylim(0, 100)
plt.show()