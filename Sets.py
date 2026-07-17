# Python Sets Practice Task 1

# Objective

# Practice using Python sets and the following operations:

# union()
# intersection()
# difference()
# Instructions
# Create two sets:
# studentsFootball containing the names of 6 students who play football.
# studentsCricket containing the names of 6 students who play cricket.
# Make sure at least 2 students are in both sets.
# Print both sets.
# Find and print the Union of the two sets.
# This should show all students who play at least one sport.
# Find and print the Intersection of the two sets.
# This should show students who play both football and cricket.
# Find and print the Difference:
# studentsFootball - studentsCricket
# studentsCricket - studentsFootball
# Add one new student to the studentsFootball set.
# Remove one student from the studentsCricket set.
# Print the updated sets.

Student_Football={"Shafi","Nafa","Muaz","Ahmad","Zian","Ashar"}

Students_Cricket={"Shafi","Maeer","Muaz","Haider","Omar","Rayan Ali"}

print(Student_Football)

print(Students_Cricket)

All_Sports=Student_Football | Students_Cricket

print("\nUnion Of Students:",All_Sports)

Common_Players=Student_Football & Students_Cricket

print("\nIntersesion of Students:",Common_Players)

Subraction_of_Players=Student_Football - Students_Cricket

print("\nSubtraction of Students:",Subraction_of_Players)
