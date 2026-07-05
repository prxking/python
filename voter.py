voter_count=int(input("Enter the number of potential voters: "))
for i in range(voter_count):
    voter_name = input("Enter the name of the voter: ")
    voter_age=int(input("Enter the age of the voter: "))
    if voter_age>=18:
        print(f"{voter_name} is eligible to vote.")
    else:
        print(f"{voter_name} is not eligible to vote.")