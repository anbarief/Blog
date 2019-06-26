#intro to variables, string, and print function

print("My 1st Python class")

text = "My 1st Python class"
print(text)

x = "My 1st Python class"
print(x)

print(y); print(!); print(12);

#
pi = 3.14159
radius = 2.2
# area of circle  <- this is a comment
area = pi*(radius**2) # or pi*radius*radius
print(area)

# change values of radius <- another comment
# use comments to help others understand what you are doing in code
radius = radius + 1
print(area)     # area doesn't change
area = pi*(radius**2)
print(area)

#####

for i in range(10):
    print("Repeating 10 times..")

for i in range(100):
    print("Repeating 100 times..")

for i in range(10):
    print(i)

#####

pi = 3.14159
radius = 1
area = pi*(radius**2) # or pi*radius*radius
print(area)

for i in range(15):
    radius = radius + (i+1)
    area = pi*(radius**2)
    print(area)
