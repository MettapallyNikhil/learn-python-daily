for i in range(10):
    if i == 4:
        break
    print(i, end="")

for i in range(10):
    if i == 4:
        continue
    print(i, end="")

for i in range(10):
    if i == 4 or i == 6:
        continue
    print(i)

#while loop
i = 1
while i<=10:
    if i == 4:
        i+=1
        continue
    print(i, end="")
    i+=1

for i in range(10):
    pass