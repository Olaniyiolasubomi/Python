str = "Introduction to Python Variable"
print(str)
print(len(str))
to_upper = "god is very wonderful"
print(to_upper.upper())
to_lower = "IFERG IS THE BEST CALL OF DUTY PLAYER"
print(to_lower.lower())
text = "call of duty players"
print(text.title())
print(text.capitalize())
#ANY TIME THAT YOU ADD A DOT AFTER A VARIABLE IS CALLED A METHOD

#CONCATINATION
name = "Victor"
age = 35
#print(name + " is " + age + " years old")
print(f"{name} is {age} years old")
#the use of "f" is known as string formatting

#HOW TO GET INPUT FROM A USER
input = input("Please enter your name")
print(f"{input} is welcome to the room")