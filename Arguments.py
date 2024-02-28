# def Talk(*Names):
#     for Name in Names:
#         print("Hello, " + Name, end=" ")
#
# Talk("Moises", "Mac", "Kram.", "Paul")

# def Name(FName, LName):
#     print(FName + " " + LName)
#
# Name(LName = "Paule", FName= "Moises")

# def Family(*FName, LName):
#         for member in FName:
#             print(member + " " + LName)
# Family("Moises", "Mark", "rae", "Ric", LName="Paule")

# def printStudent(**student):
#     print(student["name"], student["age"])
#     print(student["course"])
#
# printStudent(name = "Moises", age = 18, course = "BSCS")


def  summationOfTen(*numbers):
    sum =0

    for i in numbers:
            sum += i
    return sum

result = summationOfTen(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Sum of ten consecutive numbers: ", result)

def summation(*numbers):
  even_sum = 0
  odd_sum = 0

  for num in numbers:
    if num % 2 == 0:
      even_sum += num
    else:
      odd_sum += num

  # Return the calculated sums after the loop iterates through all numbers
  return even_sum, odd_sum

# Example usage
result_even, result_odd = summation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Sum of even numbers:", result_even)  # Output: 30
print("Sum of odd numbers:", result_odd)   # Output: 25

def passwordCheck(*word, Matcher):
    for password in word:
        if password == Matcher:
            print("Password Matched")
        else:
            print("Password does not match")

passwordCheck("123", 123, "abc", "23b", Matcher = 123)