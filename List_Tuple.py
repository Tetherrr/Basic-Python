#read n write collection of variables
courses = ["BSIS", "BSCS", "BSCPE"]
print(courses)

#There are  + and - index
# + starts at 0, 1, 2
# - starts at -3, -2, -1

print(courses[0])
print(courses[-3])

# List Range
print(courses[ 0 : 2])
print(courses[ 2 :]) # index 2 to end of list
print(courses[ : 3]) # start of index to end of list
print(courses[ 0 : 1]) # indet 0 to 1

# Changing Values
courses[0] = "BSTM" # BSIS is replaced with BSTM

print(courses)
print(len(courses))

# Count on list
print(courses.count("BSCS"))

#Add Items on list by using APPEND(),adds value at end of the list
print(courses.append("BSA"))
print(courses.insert(0, "BSIT"))

#Remove items by using REMOVE()
print(courses.remove("BSA"))
# print(courses.pop(0, "BSA")) # if index is not indicated thenit removes forn the end of the list

#Deletes list
# del courses[0]
# del courses

#Clear list
# courses.clear() #Deletes items inside list but still can be accessed

#Copy List to another
x = courses.copy()
print(x)


listSum = courses + x
print(listSum)

#extend() combines list to the end of the first list
courses.extend(x)
print(courses)

#Sort List
courses.reverse()
courses.sort() #Ascend
courses.sort(reverse= True) #Descend

#Nested List
num = [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]] #Nested list is index 5

print(num[5][1])

numTwo = [1, 2, 3, 4, 5, [6, 7, 8, 9, 10, [100, 200]]]
print(numTwo[5][5][1]) # Output : 200

#Tuples are read Only, Combined, delete as whole,cannot be manipulated individually
numEven = (2, 4, 6, 8, 10)
numEven = list(numEven)
print(numEven)