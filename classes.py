class student:
    no_of_leaves = 10
    pass


harry = student()
larry = student()
harry.name = "HARRY"
harry.section = "B"
harry.std = 12
print(harry.no_of_leaves)
student.no_of_leaves = 15
print(harry.no_of_leaves)
larry.name = "LARRY"
larry.section = "C"
larry.std = 11

print(harry.name)
print(harry.std)
print(larry.name)
print(harry.section)
