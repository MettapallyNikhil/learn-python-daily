L=[10,20,30,40,50, "Nikhil is Great"]

for i in L:
    print(i)

for i in L:
    print(i,type(i))

for i in [10,20,30,40,50, "Nikhil is Great"]:
    print(i,type(i))

#nest for loop
numlist=[1,2,3]
charlist=["a","b","c","d"]

for n in numlist:
    print(n)
    for c in charlist:
        print(c)

L=[10,20,30,40,50, "Nikhil is Great"]

for i in L:
    print(i)
    for i in L:
        print(i)


i=1
while i<=10:
    print(i)
    i+=1    #i=i+1

i=1
while i<=10:
    print(i, end="")
    i+=1    #i=i+1