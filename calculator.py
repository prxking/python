
while True:
    print("Select the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit\n")
    a = int(input("Enter the first operand: "))
    b = int(input("Enter the second operand: "))

    choice = int(input("Enter your choice: "))
    print() # Adds a clean line break
        
    if choice == 1:
        print(f"The sum of {a} and {b} is {a + b}\n")
    elif choice == 2:
        print(f"The difference of {a} and {b} is {a - b}\n")        
    elif choice == 3:
        print(f"The product of {a} and {b} is {a * b}\n")
    elif choice == 4:
        if b != 0:
            print(f"The quotient of {a} and {b} is {a / b}\n")
        else:
            print("Division by zero is not allowed\n")
    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break
    else:  
        print("Invalid choice. Please try again.\n")  

# Run the program
