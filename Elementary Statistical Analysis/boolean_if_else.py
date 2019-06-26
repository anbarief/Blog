#
i = 10; j = -2;

print(i > j)
print(i >= j)
print(i < j)
print(j < i)
print(i <= j)

print(i == j)
print(i != j)

x = i>=j
y = i==j
print(not x)
print(not y)
print(x and y)
print(True and True)
print(False and True)
print(x or y)
print(True or False)

print(100 < 1002)
print(5*4*3 > 4*4*4)

#

if (1 < 10):
    print("1 is less than 10")

if (1 < 10):
    print("1 is less than 10")
else:
    print("1 is not less than 10")

x = 10

if (x < 0): # x > 0 ?
    print("x is negative")
elif (x >= 0 and x < 5):
    print("x is nonnegative but less than 5")
elif (x == 5):
    print("x is 5")
else:
    print("x is more than 5")
    
#
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))

if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, x / y is", 1)
        
elif x < y:
    print("x is smaller")

else:
    print("y is smaller")

print("thanks!")
