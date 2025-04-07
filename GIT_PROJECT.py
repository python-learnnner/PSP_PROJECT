import tkinter
from tkinter import messagebox

window=tkinter.Tk()
window.title("Login System")
window.geometry("400x300")
window.configure(bg="white")

def login():
    username=username_entry.get()
    password=password_entry.get()
    if username=="Bibek Ale" and password=="imusttelljesus":  # Example credentials
        tkinter.messagebox.showinfo("Login Successful",f"Welcome {username}!" )
    else:
        tkinter.messagebox.showerror("Login Failed", "Invalid username or password.")
  

frame=tkinter.Frame(bg="white")

#Creating widgets on the screen
login_label=tkinter.Label(frame,text="Login",font=("times new roman",20,"bold"),bg="white",fg="black")
username_label=tkinter.Label(frame,text="Username",font=("times new roman",12,"bold"),bg="white",fg="black")
username_entry=tkinter.Entry(frame,font=("times new roman",12,"bold"),bg="white",fg="black")
password_entry=tkinter.Entry(frame,font=("times new roman",12,"bold"),bg="white",fg="black",show="*")
password_label=tkinter.Label(frame,text="Password",font=("times new roman",12,"bold"),bg="white",fg="black")
login_button=tkinter.Button(frame,text="Login",font=("times new roman",12,"bold"),bg="Blue",fg="White",command=login)


#Placing widgets on the screen
login_label.grid(row=0,column=1,pady=10)
username_label.grid(row=1,column=0,pady=10)
username_entry.grid(row=1,column=1,pady=10)
password_label.grid(row=2,column=0,pady=10)
password_entry.grid(row=2,column=1,pady=10)
login_button.grid(row=3,column=1,pady=10)

frame.pack()

window.mainloop()