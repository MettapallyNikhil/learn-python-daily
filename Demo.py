print("Hello, World!")
a = 5
b = 10
print('sum is:', a + b)

#Single line comment is # and multi line comment is ''' ''' or """ """
#Comments
'''If we want dont want to execute the code below we can use comments'''

#keywords or reserved words - we need to use these words as it is, as it is an Case sensitive language
import keyword
print(keyword.kwlist)

#Indentation
'''To consider the If and Else statements we need to use indentation
(we can use single space or multiple spaces but we need to be consistent) '''
n = 10
if n==52:
    print('True')
else:
    print('False')

#Identifiers
'''Rules to create identifiers
1. Case Sensitive
2. Lowercase and Uppercase letters, 
3. Digits and underscore(_) are allowed
4. Cannot start with a digit
5. Cannot use keywords/reserved words
6. Cannot use special characters like @, $, %, etc
7. Cannot use spaces, shouldnt be in 2 parts'''

#Variables
''' 1. its an identifier
    2. Its an named memory location to store data
    3. no need specify the datatype '''
print(n)
print(type(n))

#Multiple assignment
a=b=c=10
print(a,b,c)
print(a,b,c, sep=',')

#Datatypes
#Type casting - converting one datatype to another datatype
input('enter Input number:')
print(type(a))
input('enter Input number:')
print(type(b))
c = a+b
print('The result is:', c)

a = int(input('enter Input number:'))
print(type(a))

b = int(input('enter Input number:'))
print(type(b))

c = a + b
print('The result is:', c)