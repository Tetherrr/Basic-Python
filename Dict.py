#Collection of key pairs, unordered changeable and indexed

StudentOne = {
    "Name" : "Mac",
    "Course" : "BSIT",
    "Age" : 19
}

StudentTwo = {
    "Name" : "Moi",
    "Course" : "BSCS",
    "Age" : 20

}

#Dict Lenght
print(len(StudentOne))
print(len(StudentTwo))

#Reading Dicts
#1. Reading whole Dicts
print(StudentOne)
print(StudentTwo)

#Read by key : value
print(StudentOne["Name"])#Prints Mac

#Read by item.get()
print(StudentTwo.get("Name"))#Prints Mois

#Manipulate value
StudentOne["Course"] = "BSTM"
StudentTwo["Age"] = 100

#Adding Items on Dict
StudentOne["Gender"] = "Male"

#Deleting ITEMS
StudentOne.pop("Name")
print(StudentOne)

StudentOne.popitem()# Python 3.7 deletes randomly. Now it deletes last items.
print(StudentOne)

StudentTwo.clear()#Clears whole dictionary

#Copying Dict items
StudentThree = StudentTwo.copy()
print(StudentThree)

#Getting keys only
print(StudentThree.keys())
#Values only
print(StudentThree.values())

#Dict inside list
Students = [StudentOne, StudentTwo]
print(Students[1].get("Name"))

#Nested Dict (Dict within Dict)
StudentFourAttribute ={
    "Height" : 167,
    "Weight" : 55,
    "Skin_Tone" : "Brown"

}

StudentFour = {
    "Attribute" : StudentFourAttribute
}

print(StudentFour)
print(StudentFour.get("Attribute").get("Weight"))