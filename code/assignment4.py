#initializing the seating arrangement
seat_position = [[False]*5 for _ in range(3)]

#Displaying the seating arrangement
def display_seat(seat_position):
    print("\nCurrent Seating Arrangement:")
    for row_index, row in enumerate(seat_position):
        row_display=" ".join(["Booked         " if seat_position else "Available\t" for seat_position in row])
        print(f"Row{row_index+1}:{row_display}")


#Starting the Booking Process
while True:
    display_seat(seat_position)

    command = input("Enter 'exit' to stop or press enter to continue:")
    if command.lower() == "exit":
        break

    try:
        row = int(input("Select row number (1-3):"))-1
        seat = int(input("Select seat number (1-5):"))-1

        if not seat_position [row][seat]:
            seat_position[row][seat]=True
            print("Seat booked successfully.")
        else:
            print("This seat is already booked, please select another seat.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for row and seat numbers")
    except IndexError:
        print("Invalid input. Please enter a number within the given range")

#End of Booking Process
display_seat(seat_position)
print("Booking Process Ends Here.")







