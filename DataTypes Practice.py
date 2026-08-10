d = {1:'one', 2:'two', 3:'three'}
print(d)
print(type(d))  # This will print <class 'dict'> because d is a dictionary

d = {1:'one', 1:'two', 3:'three'}
print(d)
print(type(d))  # This will print <class 'dict'> because d is a dictionary

r = range(500) # we can mention start and stop value
print(list(r)) 
print(type(r))  # This will print <class 'range'> because r is a range object