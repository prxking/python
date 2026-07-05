pin=int(input("Enter your 4-digit PIN: "))
if pin==1234:
    print("PIN accepted. Welcome to your account.")

attempts = 0 
while True:   
    if pin==1234:
        print("\n1. Balance Check\n2. Withdrawal\n3. Deposit\n4. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            print("Your balance is $1000.")
            continue
        elif choice==2:
            amount=float(input("Enter the amount to withdraw: "))
            if amount<=1000:
                print(f"You have withdrawn ${amount}. Your new balance is ${1000-amount}.")
            else:
                print("Insufficient funds.")
        elif choice==3:            
            amount=float(input("Enter the amount to deposit: "))
            print(f"You have deposited ${amount}. Your new balance is ${1000+amount}.")
        elif choice==4:
            print("Thank you for using our ATM. Goodbye!")
            break   

    elif pin!=1234 and attempts<2:  
         print("Incorrect PIN. Please try again.")
         pin=int(input("Enter your 4-digit PIN: "))
         attempts += 1              
         continue
    else:   
        print("Too many incorrect attempts. Your account is locked.")
        break                       