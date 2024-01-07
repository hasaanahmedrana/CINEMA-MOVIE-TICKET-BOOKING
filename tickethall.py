import tkinter as tk
from tkinter import simpledialog, messagebox

class SeatReservation:
    def __init__(self, root):
        self.root = root
        self.root.title("Seat Reservation")
        self.root.geometry("996x560+90+50")
        self.root.configure(bg="#C72928")

        self.seats_file_path = "booked_seats.txt"
        self.num_seats = 0
        self.booked_seats = set()
        self.create_input_bars()

    def create_input_bars(self):
        # Entry for the number of seats
        tk.Label(self.root, text="Enter the number of seats you want to book:",
                 bg="#C72928", fg="white", font=("Helvetica", 15, 'bold')).pack(pady=(0, 12))
        self.num_seats_entry = tk.Entry(self.root, width=12)
        self.num_seats_entry.pack(pady=(0, 12))

        # Button to trigger seat booking
        tk.Button(self.root, text="Book Seats", command=self.initiate_booking).pack(pady=(0, 20))

    def initiate_booking(self):
        num_seats_requested = self.num_seats_entry.get()
        try:
            self.num_seats = int(num_seats_requested)
            if 1 <= self.num_seats <= 100:
                self.create_seat_grid()
            else:
                messagebox.showwarning("Invalid Input", "You can only Select maximum 100 seats :)")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def create_seat_grid(self):
        self.seat_frame = tk.Frame(self.root, bg="#FF0000")
        self.seat_frame.pack(pady=20)

        self.seat_labels = [[tk.Label(self.seat_frame, text=str(i), width=4, height=2, relief="solid", bd=1, bg="black", fg="white")
                              for i in range(j * 10 + 1, (j + 1) * 10 + 1)] for j in range(10)]

        for i in range(10):
            for j in range(10):
                self.seat_labels[i][j].grid(row=i, column=j, padx=1, pady=1)
                self.seat_labels[i][j].bind("<Button-1>", lambda event, i=i, j=j: self.select_seat(i, j))

    def update_title(self):
        booked = len(self.booked_seats)
        title = f"Seat Reservation"
        self.root.title(title)

    def select_seat(self, row, col):
        if self.num_seats > 0:
            seat_label = self.seat_labels[row][col]
            seat_number = row * 10 + col + 1

            if seat_number in self.booked_seats:
                messagebox.showwarning("Seat Already Booked", f"Seat {seat_number} is already booked. Please select another seat.")
            else:
                seat_label.config(text="X", state="disabled", bg="gray", fg="black")
                self.booked_seats.add(seat_number)
                self.num_seats -= 1
                self.update_title()

                if self.num_seats == 0:
                    self.save_booked_seats()
                    messagebox.showinfo("Booking Successful", "All seats booked successfully! Enjoy your movie.")
                    self.root.destroy()  # Close the window

    def save_booked_seats(self):
        with open(self.seats_file_path, "w") as file:
            file.write("\n".join(map(str, self.booked_seats)))


root = tk.Tk()
seat_reservation = SeatReservation(root)
root.mainloop()
