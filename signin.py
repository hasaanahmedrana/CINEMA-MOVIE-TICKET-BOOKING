from tkinter import *
from PIL import ImageTk  # require pillow for jpeg images
from tkinter import messagebox
from cinemadatabase import *


def on_sign_in():
    username = username_entry.get()
    password = pass_entry.get()
    placeholder_texts = ["Enter Username", "Enter Password", '']
    if username in placeholder_texts or password in placeholder_texts:
        messagebox.showerror("Error", "Enter username and password both")
    else:
        if not username_exits(connection, username):
            messagebox.showerror("Error", "Username does not exist")
        else:
            if login_authentication(connection, username, password):
                messagebox.showinfo("Login Successful", "Login Successful")
                window.destroy()
                import movies
            else:
                messagebox.showerror("Error", "Invalid username or password")


def open_signup():
    window.destroy()
    import signup


def open_forget_password():
    window.destroy()
    import forget_password


#-----------------SIGNUP PAGE-----------------
window = Tk()
window.title("Login Page.")
window.geometry("996x560+90+50")
window.resizable(False, False)

#setting background image
bgimage = ImageTk.PhotoImage(file='bg2.jpg')
bglabel = Label(window, image=bgimage)
bglabel.place(x=0, y=0)

#HEADER PORTION
header = Label(window, text='LOGIN:')
header.config(font=("Helvetica", 30, 'bold'), bg="#C72928", fg='white')
header.place(x=175, y=60)
#white line below header
frame1 = Frame(window, width=450, height=2, bg="white")
frame1.place(x=50, y=135)

#USERNAME
username_label = Label(window, text='Username:')
username_label.config(font=("Helvetica", 12, 'bold'), bg="#C72928", fg='white')
username_label.place(x=100, y=180)
username_entry = Entry(window, width=20, font=("Helvetica", 11), fg='black')
username_entry.place(x=210, y=180)
#placeholder
username_entry.insert(0, "Enter Username")
#delete placeholder on click
username_entry.bind("<Button-1>", lambda event: username_entry.delete(0, END))

#PASSWORD
pass_label = Label(window, text='Password:')
pass_label.config(font=("Helvetica", 12, 'bold'), bg="#C72928", fg='white')
pass_label.place(x=100, y=220)
pass_entry = Entry(window, width=20, font=("Helvetica", 11), fg='black')
pass_entry.place(x=210, y=220)
#placeholder
pass_entry.insert(0, "Enter Password")
#delete placeholder on click
pass_entry.bind("<Button-1>", lambda event: pass_entry.delete(0, END))

#LOGIN BUTTON
login_button = Button(window, text='LOGIN', width=9, font=("Helvetica", 9, 'bold'), bg="white", fg='#C72928',
                      command=on_sign_in)
login_button.place(x=200, y=260)

frame2 = Frame(window, width=450, height=1, bg="white")
frame2.place(x=50, y=315)

#CHANGE PASSWORD
f_pass_label = Label(window, text='In case you forget your password, change it.',
                       bg="#C72928", fg='white', font=("Helvetica", 12, 'bold'))
f_pass_label.place(x=80, y=335)
forget_button = Button(window, text='Forget Password', width=15,
                    font=("Helvetica", 10, 'bold'), bg="white", fg='#C72928', command=open_forget_password)
forget_button.place(x=170, y=365)

frame3 = Frame(window, width=450, height=1, bg="white")
frame3.place(x=50, y=415)

#Register Button
register_label = Label(window, text='If you are not already registered, Please register .',
                       bg="#C72928", fg='white', font=("Helvetica", 12, 'bold'))
register_label.place(x=77, y=430)
register_button = Button(window, text='Register', width=10,  font=("Helvetica", 10, 'bold'),
                         bg="white", fg='#C72928', command=open_signup)
register_button.place(x=190, y=465)
frame4 = Frame(window, width=450, height=1, bg="white")
frame4.place(x=50, y=510)

#CLOSE
window.mainloop()
