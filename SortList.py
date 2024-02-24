

numList = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


evenList = " "
oddList = " "

evenSort = []

oddSort = []

for x in range(len(numList)):
    if numList[x] % 2 == 0:
        evenList += str(numList[x]) + ", "
        evenSort.append( numList[x])
    else:
        oddList += str(numList[x]) + ", "
        oddSort.append( numList[x] )

else:
    print("Processing Sort")

print("Even : " + (evenList))
print("Odd : " + (oddList))


evenSort.reverse()
print("Even Descend: ", evenSort)

oddSort.reverse()
print("Odd Descend: ", oddSort)