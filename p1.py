def addition(num1,num2): 
     return num1+num2
def subraction(num1,num2):
    return num1-num2 
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2   
#program to find shot out calculator arithmetic operations
print("+ = addition")
print("-=subraction")
print("* = mutliplication")
print("/=division")
print(" ""  =exit ")
while (True):
 choice=input("Enter a operator  to do on the value:")
 if choice == "+": 
   value1=int(input("Enter a value1:"))
   value2=int(input("Enter a value2:"))
   print("The result is ",addition(value1,value2))
 elif choice =="-":
   value1=int(input("Enter a value1:"))
   value2=int(input("Enter a value2:"))
   print("The result is",subraction(value1,value2))
 elif choice == "*":
   value1=int(input("Enter a value1:"))
   value2=int(input("Enter a value2:"))
   print("The result is",multiplication(value1,value2)) 
 elif choice == "/":
   value1=int(input("Enter a value1:"))
   value2=int(input("Enter a value2:"))
   print("The result is ",division(value1,value2))   
 elif choice == "":
    print("Thanks for using try again")
    break   
 else:
    print("your input is invalid.Please enter a valid operator that mentioned.")
     