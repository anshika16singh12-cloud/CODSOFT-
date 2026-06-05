# Calculator Program

print("==== SIMPLE CALCULATOR ====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Choose an operation (1-4):"))
result = 0
if (choice in [1,2,3,4]):
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))

    if(choice == 1):
        result = num1 + num2
        operation = "Addition"

    elif(choice == 2):
        result = num1 - num2
        operation = "Subtraction"

    elif(choice == 3):
        result = num1 * num2
        operation = "Multiplication"

    elif(choice == 4):
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            exit()
        result = num1 / num2
        operation = "Division"

else:
    print("Invalid choice. Please select a number between 1 and 4.")

print("The result of the operation is {}".format(result))
