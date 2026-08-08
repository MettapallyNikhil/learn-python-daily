a = input("Enter a number for a: ")  
print(type(a))  # This will print <class 'str'> because input() returns a string
b = input("Enter a number for b: ")
print(type(b))  # This will also print <class 'str'>
c = a + b
print("The sum of a and b is:", c)
#because they are of the string type, thats why the output will be concatenated instead of summed.
#to fix this we need type casting.

#in bool T is 1 and F is 0.
a=10
b=20
c=a<b
print(c)  # This will print True because 10 is less than 20
print(type(c))  # This will print <class 'bool'> because c is a boolean value   

print(True+1)
print(True+21)

#complex - real and imaginary parts
a=10
b=20
c=complex(a,b)
print(c)  # This will print (10+20j) because c is a complex number with real part 10 and imaginary part 20
#we can add two complex numbers
#we use in matplotlib and numpy for complex numbers.
a= 1+2j
b= 2+3j
c= a + b