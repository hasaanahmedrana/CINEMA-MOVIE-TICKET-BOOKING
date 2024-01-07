from tkinter import *
from tkinter import ttk
import cinemadatabase
from PIL import ImageTk  # require pillow for jpeg images
from tkinter import messagebox


# Function to open the ticket hall page
def open_ticket_hall():
    window4.destroy()
    import tickethall


#--------------------GUI-----------------------
# Create a window
window4 = Tk()
window4.title("Movie Page.")
window4.geometry("996x560+90+50")
window4.resizable(False, False)

#setting background image
bgimage = ImageTk.PhotoImage(file='bg3.jpg')
bglabel = Label(window4, image=bgimage)
bglabel.place(x=0, y=0)


#HEADER PORTION
tree = ttk.Treeview(window4, height=12)

# Define Our Columns
tree['columns'] = ('ID', 'Movie title', 'Genre', 'Rating', 'Ticket Price')

# Format our columns
tree.column("#0", width=0, stretch=NO)
tree.column("ID", anchor=CENTER, width=80)
tree.column("Movie title", anchor=CENTER, width=120)
tree.column("Genre", anchor=CENTER, width=100)
tree.column("Rating", anchor=CENTER, width=100)
tree.column("Ticket Price", anchor=CENTER, width=100)

tree.heading("#0", text="", anchor=CENTER)
tree.heading("ID", text="ID", anchor=CENTER)
tree.heading("Movie title", text="Movie title", anchor=CENTER)
tree.heading("Genre", text="Genre", anchor=CENTER)
tree.heading("Rating", text="Rating", anchor=CENTER)
tree.heading("Ticket Price", text="Ticket Price", anchor=CENTER)


# Set the heading for each column
for col in tree['columns']:
    tree.heading(col, text=col)


# Insert some data
def insert_data():
    data = cinemadatabase.view_all_movies(cinemadatabase.connection)
    for row in data:
        tree.insert("", "end", values=row)
insert_data()


def clear_selection():
    movie_entry.delete(0, END)
    tree.selection_remove(tree.selection()[0])

def on_tree_select(event):
    if tree.selection():
        selected_item = tree.selection()[0]
        # Get the values of the selected row
        selected_values = tree.item(selected_item, "values")
        #displaying the selected movie
        movie_name = selected_values[1]
        clear_selection()
        movie_entry.insert(0, movie_name)

    else:
        pass

# Bind the function to the treeview
tree.bind('<<TreeviewSelect>>', on_tree_select)


# Place the treeview at the middle left of the window
tree.place(x=250, y=40)

# Create a scrollbar
scrollbar = ttk.Scrollbar(window4, orient=VERTICAL, command=tree.yview)
# Place the scrollbar
scrollbar.place(x=785, y=35, height=280)

#Selected movie Entry
movie_entry = Entry(window4, width=30, borderwidth=3)
movie_label = Label(window4, text="Selected Movie", font=("Arial", 12,'bold'),fg="white", bg="black")
movie_entry.place(x=480, y=320)
movie_label.place(x=330, y=320)

# Create a Button to confirm movie selection and move to the select ticket hall page
confirm_button = Button(window4, text="NEXT", command=open_ticket_hall)
confirm_button.config(font=("Arial", 15,'bold'),fg="RED", bg="WHITE",command=open_ticket_hall)
# Place the Button
confirm_button.place(x=470, y=400)

window4.mainloop()
