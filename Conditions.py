Grade1 = (float(input("Enter 1st Grade: ")))
Grade2 = (float(input("Enter 2nd Grade: ")))
Grade3 = (float(input("Enter 3rd Grade: ")))

Average = (Grade1 + Grade2 + Grade3)/3
average = float(round(Average, 2))

if average >100 and average <= 50:
    print("Average Grade: ", average, "Invalid Grade!")
elif average >= 98 and average <= 100:
        print("Average Grade: ", average, "With Highest Honor")
elif average >=95 and average <= 97:
    print("Average Grade: ", average, "With High Honors")
elif average >=90 and average <=94:
    print("Average Grade: ", average, "With Honors")
elif average >=75 and average <=89:
    print("Average Grade: ", average, "Passed")
else:
    print("Average Grade: ", average, "Failed")

evenList = [2, 4, 6, 1, 8, 10, 12]
if 1 in evenList:
    print("1 is an even number!")
else:
    print("All Numbers on the list is even")



