class Train:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = list(range(1, total_seats))
        self.booked_seats = []
    
    def show_available_seats(self):
        if self.available_seats:
            print(f"Available seats {self.available_seats}")
        else:
            print("No seats are available")

    def book_seat(self, seat_number):
        if seat_number in self.available_seats:
            self.available_seats.remove(seat_number)
            self.booked_seats.append(seat_number)
            print(f'The seat {seat_number} has been booked')
        else:
            print("The seat has already been booked...")
    def delete_seat(self, seat_number):
        if seat_number in self.booked_seats:
            self.booked_seats.remove(seat_number)
            self.available_seats.append(seat_number)
            print(f"The seat {seat_number} has successfully deleted")
        else:
            print("The seat is already free or cannot be deleted...")
def show_menu():
    print("1. Show Available seats")
    print("2. Book a ticket")
    print("3. Cancel a ticket")
    print("4. Exit")

def main():
    train = Train(20)

    while True:
        show_menu()
        choice = int(input("Enter a choice : "))
        if choice == 1:
            train.show_available_seats()
        elif choice == 2:
            try:
                seat_number = int(input("Enter the seat number : "))
                train.book_seat(seat_number)
            except valueError:
                print("Invalid number")
        elif choice == 3:
            try:
                seat_number = int(input("Enter the seat number : "))
                train.delete_seat(seat_number)
            except valueError:
                print("Cannot be deleted")
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice")
        

                
if __name__ == "__main__":
    main()

