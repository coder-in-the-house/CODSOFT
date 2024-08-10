import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, master):
        self.contacts = {}
        self.master = master
        self.master.title("Contact Book")

        # Initialize the interface
        self.setup_interface()

    def setup_interface(self):
        # Labels and input fields
        tk.Label(self.master, text="Full Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_input = tk.Entry(self.master, width=30)
        self.name_input.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.master, text="Phone Number:").grid(row=1, column=0, padx=10, pady=5)
        self.phone_input = tk.Entry(self.master, width=30)
        self.phone_input.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.master, text="Email Address:").grid(row=2, column=0, padx=10, pady=5)
        self.email_input = tk.Entry(self.master, width=30)
        self.email_input.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.master, text="Home Address:").grid(row=3, column=0, padx=10, pady=5)
        self.address_input = tk.Entry(self.master, width=30)
        self.address_input.grid(row=3, column=1, padx=10, pady=5)

        # Buttons for actions
        tk.Button(self.master, text="Add Entry", command=self.add_entry).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(self.master, text="Show All", command=self.show_entries).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.master, text="Find Entry", command=self.find_entry).grid(row=5, column=0, padx=10, pady=10)
        tk.Button(self.master, text="Edit Entry", command=self.edit_entry).grid(row=5, column=1, padx=10, pady=10)
        tk.Button(self.master, text="Remove Entry", command=self.remove_entry).grid(row=6, column=0, padx=10, pady=10)
        tk.Button(self.master, text="Exit", command=self.master.quit).grid(row=6, column=1, padx=10, pady=10)

        # Output display area
        self.result_display = tk.Text(self.master, height=10, width=50)
        self.result_display.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def add_entry(self):
        name = self.name_input.get()
        phone = self.phone_input.get()
        email = self.email_input.get()
        address = self.address_input.get()

        if not name or not phone:
            messagebox.showwarning("Input Error", "Both name and phone number are required.")
            return

        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }

        messagebox.showinfo("Success", "Contact successfully added!")
        self.clear_inputs()

    def show_entries(self):
        self.result_display.delete(1.0, tk.END)
        for name, details in self.contacts.items():
            self.result_display.insert(tk.END, f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n\n")

    def find_entry(self):
        query = simpledialog.askstring("Search", "Enter name or phone number to search:")
        if not query:
            return

        self.result_display.delete(1.0, tk.END)
        found = False
        for name, details in self.contacts.items():
            if query in name or query in details["phone"]:
                self.result_display.insert(tk.END, f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n\n")
                found = True

        if not found:
            self.result_display.insert(tk.END, "No matching contacts found.")

    def edit_entry(self):
        name = simpledialog.askstring("Edit Contact", "Enter the name of the contact to update:")
        if not name or name not in self.contacts:
            messagebox.showwarning("Error", "Contact not found.")
            return

        new_phone = simpledialog.askstring("Update Phone", "Enter new phone number:")
        new_email = simpledialog.askstring("Update Email", "Enter new email address:")
        new_address = simpledialog.askstring("Update Address", "Enter new address:")

        if new_phone:
            self.contacts[name]["phone"] = new_phone
        if new_email:
            self.contacts[name]["email"] = new_email
        if new_address:
            self.contacts[name]["address"] = new_address

        messagebox.showinfo("Updated", "Contact details updated successfully!")

    def remove_entry(self):
        name = simpledialog.askstring("Delete Contact", "Enter the name of the contact to delete:")
        if not name or name not in self.contacts:
            messagebox.showwarning("Error", "Contact not found.")
            return

        del self.contacts[name]
        messagebox.showinfo("Removed", "Contact deleted successfully!")

    def clear_inputs(self):
        self.name_input.delete(0, tk.END)
        self.phone_input.delete(0, tk.END)
        self.email_input.delete(0, tk.END)
        self.address_input.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
