# Accept the number of units consumed
units = float(input("Enter the number of units consumed: "))

# Initialize the bill variable
bill = 0.0

# Calculate the bill using conditional statements
if units <= 100:
    # First 100 units at ₹5
    bill = units * 5

elif units <= 200:
    # First 100 units at ₹5, remaining units at ₹7
    bill = (100 * 5) + ((units - 100) * 7)

else:
    # First 100 units at ₹5, next 100 units at ₹7, remaining units at ₹10
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Display the final bill
print(f"\nTotal units consumed: {units}")
print(f"Your final electricity bill is: ₹{bill:.2f}")