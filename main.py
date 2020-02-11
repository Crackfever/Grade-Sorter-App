print("Welcome to the Grade Sorter App")

#Start list and get user input
grades = []
grade = (input("\nWhat is your first grade (0-100): "))
grades.append(grade)
grade = (input("What is your second grade (0-100): "))
grades.append(grade)
grade = (input("What is your third grade (0-100): "))
grades.append(grade)
grade = (input("What is your forth grade (0-100): "))
grades.append(grade)

print("\nYour grades are: " + str(grades))

#Sort list high to low
grades.sort(reverse=True)
print("\nYour grades from highest to lowest are: " + str(grades))

#Removing lowest 2 grades
print("\nThe lowest two grades will now be dropped.")
removed_grade = grades.pop()
print("Removed grade: " + str(removed_grade))
removed_grade = grades.pop()
print("Removed grade: " + str(removed_grade))

#Recap remaining grades
print("\nYour remaining grades are: " + str(grades))
print("Nice work! Your highest grade is " + str(grades[0])+ ".")