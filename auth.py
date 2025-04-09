import tkinter as tk
from tkinter import ttk, messagebox
from user_view import LoginSystem, users  # Assumes user.py handles LoginSystem & users

class AuthSystem(LoginSystem):
    def __init__(self, root):
        super().__init__(root)
        self.tickets = [
            {"id": 1, "event": "Concert", "date": "2023-12-15", "price": "$50", "status": "Available"},
            {"id": 2, "event": "Theater Play", "date": "2023-12-20", "price": "$35", "status": "Sold Out"},
            {"id": 3, "event": "Sports Game", "date": "2023-12-25", "price": "$75", "status": "Available"},
            {"id": 4, "event": "Movie Premiere", "date": "2024-01-05", "price": "$25", "status": "Available"},
        ]
        self.current_user = None

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in users and users[username]["password"] == password:
            self.current_user = username
            messagebox.showinfo("Login Successful", f"Welcome {username}!")
            self.show_post_login_options()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def show_post_login_options(self):
        self.clear_frame()

        frame = tk.Frame(self.root, bg="white")
        frame.pack(expand=True)

        welcome = tk.Label(frame, text=f"Welcome, {self.current_user}!", 
                           font=("Times New Roman", 16, "bold"), bg="white", fg="black")
        welcome.pack(pady=20)

        dashboard_btn = tk.Button(frame, text="View Dashboard", font=("Times New Roman", 14),
                                  bg="blue", fg="white", command=self.show_dashboard)
        dashboard_btn.pack(pady=10, ipadx=10, ipady=5)

        update_btn = tk.Button(frame, text="Update Profile", font=("Times New Roman", 14),
                               bg="green", fg="white", command=self.show_update_profile_frame)
        update_btn.pack(pady=10, ipadx=10, ipady=5)

        logout_btn = tk.Button(frame, text="Logout", font=("Times New Roman", 12),
                               bg="red", fg="white", command=self.show_login_frame)
        logout_btn.pack(pady=20)

    def show_dashboard(self):
        self.clear_frame()

        frame = tk.Frame(self.root, bg="white")
        frame.pack(expand=True, fill=tk.BOTH)

        header = tk.Frame(frame, bg="blue")
        header.pack(fill=tk.X)

        tk.Label(header, text="Ticket Dashboard", font=("Times New Roman", 16, "bold"),
                 bg="blue", fg="white").pack(side=tk.LEFT, padx=10, pady=10)

        tk.Button(header, text="Back", command=self.show_post_login_options,
                  bg="white", fg="blue").pack(side=tk.RIGHT, padx=10)

        # Ticket treeview
        columns = ("id", "event", "date", "price", "status")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, anchor=tk.CENTER if col in ("id", "date", "price", "status") else tk.W, width=100)
        self.tree.column("event", width=150)

        # Insert data
        for ticket in self.tickets:
            self.tree.insert("", tk.END, values=(ticket["id"], ticket["event"], ticket["date"],
                                                 ticket["price"], ticket["status"]))
        self.tree.pack(padx=20, pady=10)

        tk.Button(frame, text="Purchase Selected Ticket", font=("Times New Roman", 12),
                  bg="green", fg="white", command=self.purchase_ticket).pack(pady=10)

    def show_update_profile_frame(self):
        self.clear_frame()

        frame = tk.Frame(self.root, bg="white")
        frame.pack(expand=True, fill=tk.BOTH)

        header = tk.Frame(frame, bg="blue")
        header.pack(fill=tk.X)

        tk.Button(header, text="Back", command=self.show_post_login_options,
                  bg="white", fg="blue").pack(side=tk.LEFT, padx=10, pady=5)

        tk.Label(frame, text="Update Profile", font=("Times New Roman", 18, "bold"),
                 bg="white", fg="black").pack(pady=10)

        user_data = users[self.current_user]

        self.email_update_entry = self.create_entry(frame, "Email", user_data["email"])
        self.security_q_update_entry = self.create_entry(frame, "Security Question", user_data["security_question"])
        self.security_a_update_entry = self.create_entry(frame, "Security Answer", user_data["security_answer"])
        self.password_update_entry = self.create_entry(frame, "New Password (leave blank to keep current)", "", show="*")

        tk.Button(frame, text="Update Profile", font=("Times New Roman", 12, "bold"),
                  bg="blue", fg="white", command=self.update_profile).pack(pady=15)

    def create_entry(self, parent, label, default_val="", show=None):
        tk.Label(parent, text=label, font=("Times New Roman", 12), bg="white", fg="black").pack(pady=(10, 0))
        entry = tk.Entry(parent, font=("Times New Roman", 12), bg="white", fg="black", show=show)
        entry.insert(0, default_val)
        entry.pack()
        return entry

    def update_profile(self):
        new_email = self.email_update_entry.get()
        new_security_q = self.security_q_update_entry.get()
        new_security_a = self.security_a_update_entry.get()
        new_password = self.password_update_entry.get()

        if not all([new_email, new_security_q, new_security_a]):
            messagebox.showerror("Error", "Email, security question and answer are required!")
            return

        users[self.current_user]["email"] = new_email
        users[self.current_user]["security_question"] = new_security_q
        users[self.current_user]["security_answer"] = new_security_a
        if new_password:
            users[self.current_user]["password"] = new_password

        messagebox.showinfo("Success", "Profile updated successfully!")
        self.show_post_login_options()

    def purchase_ticket(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a ticket first!")
            return

        item = self.tree.item(selected_item)
        ticket_id, event, date, price, status = item["values"]

        if status == "Sold Out":
            messagebox.showerror("Error", "This ticket is already sold out!")
            return

        for ticket in self.tickets:
            if ticket["id"] == ticket_id:
                ticket["status"] = "Sold Out"
                break

        self.show_dashboard()
        messagebox.showinfo("Success", f"You have successfully purchased a ticket for {event} on {date}!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ticket Management System")
    root.geometry("700x600")
    app = AuthSystem(root)
    root.mainloop()
