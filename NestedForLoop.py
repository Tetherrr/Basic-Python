#Prints line when inner loop is completed by each iterated condition
for x in range(2):
    x += 1
    print("New Line: " + str(x) )
    for y in range (2):
        y += 1
        print(y)

#end combines next print method
print("*", end="")
print("1")

for a in range(2):
    a += 1
    print("New Line: " + str(a) )
    for b in range (2):
        print("%", end="")
    print() #prints line for every condition satiesfied