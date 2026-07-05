secretnumber=270
i=0
while True:
    guess=int(input("Enter your guess: "))
    if guess<secretnumber:
        print("Too low! Try again.")
    elif guess>secretnumber:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {secretnumber} in {i+1} attempts.")
        break
    i+=1