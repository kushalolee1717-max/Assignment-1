print("Simple Calculator")

num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number"))

print("Choose operation")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

choice = input("Enter choice (1/2/3/4):")
if choice == "1":
    print("Result:", num1 + num2)
elif choice == "2":
    print("Result:", num1 - num2)
elif choice == "3":
    print("Result:", num1 * num2)
elif choice == "4":
    if num2 !=0:
     print("Result:", num1 / num2)
    else:
      print("Error: Cannot divide by zero")


else:
   print("Invalid Choice")