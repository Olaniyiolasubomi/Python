student = ["Joseph ", "Nicholas ", "Mbata ", "Paige ", "Victor"]
print(student[0])
print(len(student))

#SLICING has a starting and the ending but the ending is not always inclusive
#slicing with POSITIVE DIGITS will start from the begining
print(student[1:4])
#slicing with NEGETIVE DIGITS will start from the back
print(student[-4:-1])
print(student[0:4])
student[0]='David'
print(student)

#LIST METHOD

#ATTEND
student.append("Skeppy")
print(student)
#append is used to add to the end

#INSERT
student.insert(4,"Divine")
print(student)
#insert will add wherever you want

#POP
student.pop()
print(student)
#pop will remove the last item in the list
"""
#CLEAR
student.clear()
print(student)
"""

#COPY
new_student = student.copy()
print(new_student)

#INDEX
index = student.index("Divine")
print(index)

#EXTEND
list_one = [1, 2, 3, 4]
list_two = ['a' , 'b ', 'c ', 'd']
list_one.extend(list_two)
print(list_one)