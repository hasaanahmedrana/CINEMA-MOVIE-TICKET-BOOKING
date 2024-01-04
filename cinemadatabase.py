#movie
import sqlite3
connection = sqlite3.connect('database.db')


#---------------movie-----------------
def create_table(connection):
    cur = connection.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY,'
                'username TEXT,'
                ' password TEXT,'
                'phone_number INTEGER,'
                ' email TEXT)')
    connection.commit()


def add_user(connection, username, password, phone_number, email):
    cur = connection.cursor()
    if username in connection.execute('SELECT username FROM user'):
        print("Username already exists")
    else:
        cur.execute('INSERT INTO user(username, password, phone_number, email) VALUES(?,?,?,?)', (username, password, phone_number, email))
        connection.commit()
        print("User added successfully")


def changing_password(connection, username, password):
    cur = connection.cursor()
    if username in connection.execute('SELECT username FROM user'):
        cur.execute('UPDATE user SET password = ? WHERE username = ?', (password, username))
        connection.commit()
        print("Password changed successfully")
    else:
        print("Username does not exist")


def create_table(connection):
    cur = connection.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY,name TEXT, genre TEXT, rating REAL, ticket_price INTEGER, tickets_available INTEGER)')
    connection.commit()


def add_movie(connection):
    cur = connection.cursor()
    movies = [
    ("Interstellar", "Sci-Fi", 9.7, 1200, 100),
    ("The Godfather", "Crime", 9.2, 1000, 80),
    ("The Dark Knight", "Action", 9.0, 1200, 120),
    ("Pulp Fiction", "Crime", 8.9, 1200, 90),
    ("Forrest Gump", "Drama", 8.8, 1000, 110),
    ("Maula Jutt", "Drama", 8.5, 900, 150),
    ("Inception", "Sci-Fi", 8.5, 1200, 120),
    ("The Matrix", "Sci-Fi", 8.7, 1200, 100),
    ("Dangal", "Biography", 8.4, 900, 160),
    ("PK", "Comedy", 8.2, 900, 145),
    ("3 Idiots", "Comedy", 8.4, 900, 170),
    ("The Shawshank Redemption", "Drama", 9.3, 1200, 100),
    ("The Godfather: Part II", "Crime", 9.0, 1000, 80),

]

    for movie in movies:
        cur.execute('SELECT name FROM movies WHERE name = ?', (movie[0],))
        existing_movie = cur.fetchone()
        if existing_movie is None:
            cur.execute('INSERT INTO movies(name, genre, rating, ticket_price, tickets_available) VALUES(?,?,?,?,?)', movie)
    connection.commit()


def view_all_movies(connection):
    cur = connection.cursor()
    cur.execute('SELECT * FROM movies')
    t = cur.fetchall()
    connection.commit()
    return t


def update_tickets(connection, id, quantity):
    cur = connection.cursor()
    cur.execute('UPDATE movies SET tickets_available -= ? WHERE  id = ?', (id,quantity))
    connection.commit()


#--------------------user-----------------------

def create_usertable(connection):
    cur = connection.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY,username TEXT, password TEXT,phone_number INTEGER, email TEXT)')
    connection.commit()


def add_user(connection, username, password, phone_number, email):
    cur = connection.cursor()
    cur.execute('SELECT username FROM user WHERE username = ?', (username,))
    existing_user = cur.fetchone()
    if existing_user:
        print("Username already exists")
    else:
        cur.execute('INSERT INTO user(username, password, phone_number, email) VALUES(?,?,?,?)', (username, password, phone_number, email))
        connection.commit()
        print("User added successfully")


# Corrected login_authentication function
def changing_password(connection, username, password):
    cur = connection.cursor()
    if username in connection.execute('SELECT username FROM user'):
        cur.execute('UPDATE user SET password = ? WHERE username = ?', (password,username))
        connection.commit()
        print("Password changed successfully")
    else:
        print("Username does not exist")


def username_exits(connection, username):
    cur = connection.cursor()
    cur.execute('SELECT username FROM user WHERE username = ?', (username,))
    result = cur.fetchone()
    if result:
        return True
    else:
        return False



def login_authentication(connection, username, password):
    cur = connection.cursor()
    cur.execute('SELECT * FROM user WHERE username = ? AND password = ?', (username, password))
    user = cur.fetchone()
    if user:
        return True
    else:
        return False


def view_all_users(connection):
    cur = connection.cursor()
    cur.execute('SELECT * FROM user')
    t = cur.fetchall()
    connection.commit()
    return t


create_table(connection)
add_movie(connection)
x = view_all_movies(connection)
for each in x:
    print(each)
create_usertable(connection)
add_user(connection, "admin", "admin", 1234567890, "admin")
y = view_all_users(connection)
for each in y:
    print(each)
login_authentication(connection, "admin", "admin")
