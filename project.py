import tkinter as gtk
from tkinter import messagebox

# In a real application, you'd use a database for this
users = {
    "Bibek Ale": {"password": "imusttelljesus", "email": "bibek@example.com", "security_question": "Pet's name", "security_answer": "Fluffy"}
}

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("500x400")
        self.root.configure(bg="white")
        
        self.show_login_frame()
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_login_frame(self):
        self.clear_frame()
        
        frame = tk.Frame(self.root, bg="white")
        
        # Creating widgets
        login_label = tk.Label(frame, text="Login", font=("Times New Roman", 20, "bold"), bg="white", fg="black")
        
        username_label = tk.Label(frame, text="Username", font=("Times New Roman", 12), bg="white", fg="black")
        self.username_entry = tk.Entry(frame, font=("Times New Roman", 12), bg="white", fg="black")
        
        password_label = tk.Label(frame, text="Password", font=("Times New Roman", 12), bg="white", fg="black")
        self.password_entry = tk.Entry(frame, font=("Times New Roman", 12), bg="white", fg="black", show="*")
        
        login_button = tk.Button(frame, text="Login", font=("Times New Roman", 12, "bold"), 
                               bg="blue", fg="white", command=self.login)
        
        forgot_password_button = tk.Button(frame, text="Forgot Password?", font=("Times New Roman", 10), 
                                         bg="white", fg="blue", bd=0, command=self.show_forgot_password_frame)
        
        signup_button = tk.Button(frame, text="Don't have an account? Sign up", font=("Times New Roman", 10), 
                                 bg="white", fg="blue", bd=0, command=self.show_signup_frame)
        
        # Placing widgets
        login_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        username_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)
        
        password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)
        
        login_button.grid(row=3, column=0, columnspan=2, pady=15)
        forgot_password_button.grid(row=4, column=0, columnspan=2)
        signup_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        frame.pack(expand=True)
    
    def show_signup_frame(self):
        self.clear_frame()
        
        frame = tk.Frame(self.root, bg="white")
        
        # Creating widgets
        signup_label = tk.Label(frame, text="Sign Up", font=("Times New Roman", 20, "bold"), bg="white", fg="black")
        
        new_username_label = tk.Label(frame, text="Username", font=("Times New Roman", 12), bg="white", fg="black")
        self.new_username_entry = tk.Entry(frame, font=("Times New Roman", 12), bg="white", fg="black")
        
        new_password_label = tk.Label(frame, text="Password", font=("Times New Roman", 12), bg="white", fg="black")
        self.new_password_entry = tk.Entry(frame, font=("Times New Roman", 12), bg="white", fg="black", show="*")
        
        email_label = tk.Label(frame, text="Email", font=("Times New Roman", 12), bg="white", fg="black")
        self.email_entry = tk.Entry(frame, font=("Times New Roman", 12), bg="white", fg="black")
        
        security_question_label = tk.Label(frame, text="Security Question", font=("Times New Roman", 12), bg="white", fg="black")
        self.security_question_entry = tk.Entry(frame, font=("Times New Roman", 12), bg="white", fg="black")
        
        security_answer_label = tk.Label(frame, text="Answer", font=("Times New Roman", 12), bg="white", fg="black")
        self.security_answer_entry = tk.Entry(frame, font=("Times New Roman", 12), bg="white", fg="black")
        
        signup_submit_button = tk.Button(frame, text="Sign Up", font=("Times New Roman", 12, "bold"), 
                                       bg="blue", fg="white", command=self.signup)
        
        back_button = tk.Button(frame, text="Back to Login", font=("Times New Roman", 10), 
                              bg="white", fg="blue", bd=0, command=self.show_login_frame)
        
        # Placing widgets
        signup_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        new_username_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.new_username_entry.grid(row=1, column=1, padx=10, pady=5)
        
        new_password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.new_password_entry.grid(row=2, column=1, padx=10, pady=5)
        
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.email_entry.grid(row=3, column=1, padx=10, pady=5)
        
        security_question_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.security_question_entry.grid(row=4, column=1, padx=10, pady=5)
        
        security_answer_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.security_answer_entry.grid(row=5, column=1, padx=10, pady=5)
        
        signup_submit_button.grid(row=6, column=0, columnspan=2, pady=15)
        back_button.grid(row=7, column=0, columnspan=2)
        
        frame.pack(expand=True)
    
    def show_forgot_password_frame(self):
        self.clear_frame()
        
        frame = tk.Frame(self.root, bg="white")
        
        # Creating widgets
        forgot_label = tk.Label(frame, text="Forgot Password", font=("Times New Roman", 20, "bold"), bg="white", fg="black")
        
        username_label = tk.Label(frame, text="Username", font=("Times New Roman", 12), bg="white", fg="black")
        self.forgot_username_entry = tk.Entry(frame, font=("Times New Roman", 12), bg="white", fg="black")
        
        submit_button = tk.Button(frame, text="Submit", font=("Times New Roman", 12, "bold"), 
                                bg="blue", fg="white", command=self.verify_user_for_password_reset)
        
        back_button = tk.Button(frame, text="Back to Login", font=("Times New Roman", 10), 
                              bg="white", fg="blue", bd=0, command=self.show_login_frame)
        
        # Placing widgets
        forgot_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        username_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.forgot_username_entry.grid(row=1, column=1, padx=10, pady=5)
        
        submit_button.grid(row=2, column=0, columnspan=2, pady=15)
        back_button.grid(row=3, column=0, columnspan=2)
        
        frame.pack(expand=True)
    
    def show_security_question_frame(self, username):
        self.clear_frame()
        
        frame = tk.Frame(self.root, bg="white")
        
        # Creating widgets
        security_label = tk.Label(frame, text="Security Question", font=("Times New Roman", 20, "bold"), bg="white", fg="black")
        
        question_label = tk.Label(frame, text=users[username]["security_question"], font=("Times New Roman", 12, "italic"), bg="white", fg="black")
        
        answer_label = tk.Label(frame, text="Answer", font=("Times New Roman", 12), bg="white", fg="black")
        self.security_answer_entry = tk.Entry(frame, font=("Times New Roman", 12), bg="white", fg="black")
        
        submit_button = tk.Button(frame, text="Submit", font=("Times New Roman", 12, "bold"), 
                                 bg="blue", fg="white", command=lambda: self.verify_security_answer(username))
        
        # Placing widgets
        security_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        question_label.grid(row=1, column=0, columnspan=2, pady=5)
        
        answer_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.security_answer_entry.grid(row=2, column=1, padx=10, pady=5)
        
        submit_button.grid(row=3, column=0, columnspan=2, pady=15)
        
        frame.pack(expand=True)
    
    def show_reset_password_frame(self, username):
        self.clear_frame()
        
        frame = tk.Frame(self.root, bg="white")
        
        # Creating widgets
        reset_label = tk.Label(frame, text="Reset Password", font=("Times New Roman", 20, "bold"), bg="white", fg="black")
        
        new_password_label = tk.Label(frame, text="New Password", font=("Times New Roman", 12), bg="white", fg="black")
        self.new_reset_password_entry = tk.Entry(frame, font=("Times New Roman", 12), bg="white", fg="black", show="*")
        
        confirm_password_label = tk.Label(frame, text="Confirm Password", font=("Times New Roman", 12), bg="white", fg="black")
        self.confirm_reset_password_entry = tk.Entry(frame, font=("Times New Roman", 12), bg="white", fg="black", show="*")
        
        submit_button = tk.Button(frame, text="Reset Password", font=("Times New Roman", 12, "bold"), 
                                bg="blue", fg="white", command=lambda: self.reset_password(username))
        
        # Placing widgets
        reset_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        new_password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.new_reset_password_entry.grid(row=1, column=1, padx=10, pady=5)
        
        confirm_password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.confirm_reset_password_entry.grid(row=2, column=1, padx=10, pady=5)
        
        submit_button.grid(row=3, column=0, columnspan=2, pady=15)
        
        frame.pack(expand=True)
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username in users and users[username]["password"] == password:
            messagebox.showinfo("Login Successful", f"Welcome {username}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
    
    def signup(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        email = self.email_entry.get()
        security_question = self.security_question_entry.get()
        security_answer = self.security_answer_entry.get()
        
        if not all([username, password, email, security_question, security_answer]):
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if username in users:
            messagebox.showerror("Error", "Username already exists!")
            return
        
        users[username] = {
            "password": password,
            "email": email,
            "security_question": security_question,
            "security_answer": security_answer
        }
        
        messagebox.showinfo("Success", "Account created successfully!")
        self.show_login_frame()
    
    def verify_user_for_password_reset(self):
        username = self.forgot_username_entry.get()
        
        if username in users:
            self.show_security_question_frame(username)
        else:
            messagebox.showerror("Error", "Username not found!")
    
    def verify_security_answer(self, username):
        user_answer = self.security_answer_entry.get()
        
        if user_answer.lower() == users[username]["security_answer"].lower():
            self.show_reset_password_frame(username)
        else:
            messagebox.showerror("Error", "Incorrect answer!")
    
    def reset_password(self, username):
        new_password = self.new_reset_password_entry.get()
        confirm_password = self.confirm_reset_password_entry.get()
        
        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords don't match!")
            return
        
        users[username]["password"] = new_password
        messagebox.showinfo("Success", "Password reset successfully!")
        self.show_login_frame()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginSystem(root)
    root.mainloop()