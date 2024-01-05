from tkinter import *
from PIL import ImageTk  # require pillow for jpeg images
from tkinter import messagebox
from cinemadatabase import *


def on_submittion():
    username = username_entry.get()
    new_password = new_pass_entry.get()
    confirm_password = confirm_pass_entry.get()
    placeholder_texts = ["Enter Username", "Enter New Password", "Confirm Password", '']
    if username in placeholder_texts or new_password in placeholder_texts or confirm_password in placeholder_texts:
        messagebox.showerror("Error", "All fields must be filled")
    elif new_password != confirm_password:
        messagebox.showerror("Error", "Password and Confirm Password do not match")
    else:
        if not username_exits(connection, username):
            messagebox.showerror("Error", "Username does not exist")
        else:
            changing_password(connection, username, new_password)
            messagebox.showinfo("Password Changed", "Password changed successfully")
            window3.destroy()
            import signin

def back_to_signin():
    window3.destroy()
    import signin

#GUI
window3 = Tk()
window3.title("Login Page.")
window3.geometry("996x560+90+50")
window3.resizable(False, False)

# setting background image
bgimage = ImageTk.PhotoImage(file='bg2.jpg')
bglabel = Label(window3, image=bgimage)
bglabel.place(x=0, y=0)

# HEADER PORTION
header = Label(window3, text='Forgot Password')
header.config(font=("Helvetica", 25, 'bold'), bg="#C72928", fg='white')
header.place(x=140, y=60)
# white line below header
frame1 = Frame(window3, width=450, height=2, bg="white")
frame1.place(x=50, y=135)

# USERNAME
username_label = Label(window3, text='Username:')
username_label.config(font=("Helvetica", 12, 'bold'), bg="#C72928", fg='white')
username_label.place(x=130, y=180)
username_entry = Entry(window3, width=20, font=("Helvetica", 11), fg='black')
username_entry.place(x=260, y=180)
# placeholder
username_entry.insert(0, "Enter Username")
# delete placeholder on click
username_entry.bind("<Button-1>", lambda event: username_entry.delete(0, END))

# PASSWORD
new_pass_label = Label(window3, text='Set New Password:')
new_pass_label.config(font=("Helvetica", 12, 'bold'), bg="#C72928", fg='white')
new_pass_label.place(x=100, y=220)
new_pass_entry = Entry(window3, width=20, font=("Helvetica", 11), fg='black')  # Use show='*' to hide password
new_pass_entry.place(x=260, y=225)
# placeholder
new_pass_entry.insert(0, "Enter New Password")
# delete placeholder on click
new_pass_entry.bind("<Button-1>", lambda event: new_pass_entry.delete(0, END))

# CONFIRM PASSWORD
confirm_pass_label = Label(window3, text='Confirm Password:')
confirm_pass_label.config(font=("Helvetica", 12, 'bold'), bg="#C72928", fg='white')
confirm_pass_label.place(x=100, y=260)
confirm_pass_entry = Entry(window3, width=20, font=("Helvetica", 11), fg='black')
confirm_pass_entry.place(x=260, y=265)
# placeholder
confirm_pass_entry.insert(0, "Confirm Password")
# delete placeholder on click
confirm_pass_entry.bind("<Button-1>", lambda event: confirm_pass_entry.delete(0, END))

# Button
button1 = Button(window3, text='Submit',command=on_submittion)
button1.config(font=("Helvetica", 12, 'bold'), bg="#C72928", fg='white')
button1.place(x=280, y=310)

# BACK TO SIGNIN BUTTON
back_button = Button(window3, text=' GO BACK ', width=15,
                     font=("Helvetica", 10, 'bold'), bg="white", fg='#C72928',
                     command=back_to_signin)
back_button.place(x=170, y=400)

window3.mainloop()

