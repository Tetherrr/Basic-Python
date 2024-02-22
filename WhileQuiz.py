chances = 3
points = 0

while  True:

        ans = (int(input("1. 1 + 1 = ? ")))
        if ans == 2:
            print("Correct")
            points += 1
        else:
            print("Incorrect!")
            chances -= 1

        ans2 = (int(input("2. 5 * 5 = ? ")))
        if ans2 == 25:
            print("Correct")
            points += 1
        else:
            print("Incorrect!")
            chances -= 1

        ans3 = (str(input("3. Even / Odd [6]? ")))
        if ans3.lower() == "even":
            print("Correct")
            points +=1
        else:
            print("Error")
            chances -=1

        tries = (str(input("Do you want to try again? Y/N ")))
        if tries.upper() == "Y":
                print("Continued: ", points)
                continue
        elif tries.upper() == "N":
                print("Program End\n Score", points)
                break


        if chances == 0:
            print("Score", points)
            print("You Lose")
            break
else:
    print("Score", points)