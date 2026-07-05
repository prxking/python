n=int(input("How many items have u purchased?: "))
total=0
for i in range(n):
    price=float(input("Enter the price of item: "))
    total+=price
if total>5000:
    discount=total*0.20
    total-=discount
elif total>2000:
    discount=total*0.10
    total-=discount
else:
    discount=0
print(f"The total amount is {total}\nThe discount is: {discount}\n2The final cost of the items is: {total-discount}")   