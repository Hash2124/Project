import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class HotelBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Booking Page")
        self.root.geometry("400x450")

        # Title
        tk.Label(root, text="Hotel Booking Form", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Name
        tk.Label(root, text="Full Name").pack()
        self.name_entry = tk.Entry(root, width=40)
        self.name_entry.pack(pady=5)

        # Check-in Date
        tk.Label(root, text="Check-in Date (YYYY-MM-DD)").pack()
        self.checkin_entry = tk.Entry(root, width=40)
        self.checkin_entry.pack(pady=5)

        # Check-out Date
        tk.Label(root, text="Check-out Date (YYYY-MM-DD)").pack()
        self.checkout_entry = tk.Entry(root, width=40)
        self.checkout_entry.pack(pady=5)

        # Room Type
        tk.Label(root, text="Room Type").pack()
        self.room_var = tk.StringVar(value="Single")
        room_types = ["Single", "Double", "Suite"]
        tk.OptionMenu(root, self.room_var, *room_types).pack(pady=5)

        # Book Button
        tk.Button(root, text="Book Now", command=self.book_room, bg="green", fg="white", font=("Arial", 12)).pack(pady=20)

    def book_room(self):
        name = self.name_entry.get()
        checkin = self.checkin_entry.get()
        checkout = self.checkout_entry.get()
        room_type = self.room_var.get()

        if not name or not checkin or not checkout:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            checkin_date = datetime.strptime(checkin, "%Y-%m-%d")
            checkout_date = datetime.strptime(checkout, "%Y-%m-%d")
            if checkout_date <= checkin_date:
                messagebox.showerror("Error", "Check-out must be after check-in.")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
            return

        # Booking confirmed
        messagebox.showinfo("Booking Confirmed", f"Thank you {name}!\nYour {room_type} room is booked from {checkin} to {checkout}.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelBookingApp(root)
    root.mainloop()
