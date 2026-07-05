avail_seats=20
while True:
    # 1. Added a check right at the start to stop the loop if sold out
    if avail_seats == 0:
        print("All seats are booked. Please try again later.")
        break
        
    print(f"Available seats: {avail_seats}")
    req_tickets=int(input("Enter the number of tickets you want to book: "))
    remain_seats=avail_seats-req_tickets
    
    if remain_seats>=0:
        print(f"Your booking is successful! Remaining seats: {remain_seats}")
        avail_seats=remain_seats  # 2. MOVED THIS LINE UP! It only updates if successful now.
        
    elif remain_seats<0:  # 3. Tweaked this math so it catches if they asked for too many
        print(f"Sorry, not enough seats available for your booking. Only {avail_seats} seats are available.")
        
    # We removed your bottom 'else' block, because the 'if avail_seats == 0' at the top handles it now!