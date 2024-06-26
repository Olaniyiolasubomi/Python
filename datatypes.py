"""
THERE ARE 2 CATEGORIES OF DATA TYPES IN PYTHON:
*Primitive, and
*Data collection
examples of primitive:
1. string
2.boolean
3.None
4.integer
5.float
examples of data collection:
1.list
2.tuple
3.dictionary
4.set
"""
#EXAMPLES OF STRINGS
name = "Olasubomi"
school = 'G-skills'
age = '20'
print(type(name))
print(type(school))
print(type(age))
#anything inside a quote is known as a string(whether is a number or text)

#EXAMPLES OF INTEGER
age = 54
print(type(age))
#integers are also called numbers but the type is called(int) 

#EXAMPLES OF FLOAT
price = 6.7
print(type(price))
#float is an integer with decimal(generally in programming)

#EXAMPLES OF BOOLEAN
is_student = True
print(type(is_student))
is_worker = False
print(type(is_worker))
#boolean is a true or false statement and it is known as(bool)

#EXAMPLE OF NONE
none = 5*"n"
print(none)
print(type(none))
#It is used to repeat the letter you multiplied

#EXAMPLE OF LIST
#list is a way of collecting data in python
list= []
print(type(list))

courses = ["HTML", "JavaScript", "CSS", "Python"]
print(courses)
print(type(courses))

#EXAMPLE OF TUPLE
tuple = ()
print(type(tuple))

#EXAMPLE OF DICTIONARY
dict = {}
print(type(dict))

#EXAMPLE OF SET
set = {}
print(type(set))
#this it how to create a set but since it is similar to dictionary it will print
# 'dict' as the type because they are similar