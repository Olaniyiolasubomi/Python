student = {
    'Name' : 'Victor',
    'Age' : 16,
    'Course' : 'Python',
}
print(student)
print(student['Name'])
student['Age'] = 20
print(student)
#the left side is called dictionary KEYS while the right side is called dictionary VALUES
print(student.keys())
print(student.values())
print(student.items())
#to add to a dictionary you use UPDATE
student.update({'Gender':'Male'})
print(student)