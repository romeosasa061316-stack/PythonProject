students = {
"Romeo":[45, 68, 95],
"Darren":[65, 44,79],
"Jnr":[46, 92, 87],
"Beverly":[8, 45,89],
"Natasha":[87, 56,91]
}

search = input("Enter student name: ")

if search in students:
    print("Scores:", students[search])

    average = sum(students[search]) / len(students[search])
    print("Average:", average)

else:
    print("Student not found")