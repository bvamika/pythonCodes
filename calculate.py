from pickle import FLOAT

num1 = float(input(" enter a number : "))
operation = input("enter operator : ")
num2 = float(input (" enter another num : "))


if(operation == "+"):
    print(num1 + num2)
elif(operation == "-"):
    print(num1 - num2)
elif(operation == "/"):
    print(num1/num2)
elif(operation == "*"):
    print(num1*num2)
else:
    print("errrrrr")
  
