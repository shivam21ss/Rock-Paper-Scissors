import tkinter
from tkinter import *
import random
from tkinter import ttk

import mysql.connector as m

rpsdb = m.connect(host="localhost", user="root", password="Shivam@21", database="rpsdb")
cursor = rpsdb.cursor()


def update_player_info(name, score):
    if name.strip() != "":
        # Check if the player's name already exists in the database
        query = "SELECT * FROM gametable WHERE name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()

        if result:
            # Update the score for the existing player
            current_score = result[1] + score
            update_query = "UPDATE gametable SET score = %s WHERE name = %s"
            cursor.execute(update_query, (current_score, name))
        else:
            # Insert a new row for the player
            insert_query = "INSERT INTO gametable (name, score) VALUES (%s, %s)"
            cursor.execute(insert_query, (name, score))

        rpsdb.commit()
    else:
        print("Invalid name. Please enter a valid name.")


def gamewin(com, you):
    if com == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False

    elif com == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False

    elif com == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False

    elif com == you:
        return none


def update_result_label(result):
    resultLabel.config(text=result, font=("roman", 18, "bold"))


def update_comchoice_label(choice):
    comchoiceLabel.config(text=choice)


def rock_button_pressed():
    you = 'r'
    print("rock button pressed")
    randNo = random.randint(1, 3)
    if randNo == 1:
        com = 'r'
    elif randNo == 2:
        com = 'p'
    else:
        com = 's'
    game = gamewin(com, you)
    print(f"you chose: {you}")
    print(f"com chose: {com}")

    if game == True:
        update_comchoice_label(f"   COM CHOSE : scissors")
        update_result_label("* * * * * * YOU WIN* * * * * * ")
        update_player_info(name, 2)
    elif game == False:
        update_comchoice_label(f"   COM CHOSE : paper")
        update_result_label("! ! ! ! ! ! YOU LOSE ! ! ! ! ! !")
        update_player_info(name, 0)
    elif game == None:
        update_comchoice_label(f"   COM CHOSE : rock")
        update_result_label(' ' ' " " " " " " The Game is a tie" " " " " " " ' ' ')
        update_player_info(name, 1)


def paper_button_pressed():
    you = 'p'
    print("paper button pressed")
    randNo = random.randint(1, 3)
    if randNo == 1:
        com = 'r'
    elif randNo == 2:
        com = 'p'
    else:
        com = 's'

    game = gamewin(com, you)
    print(f"you chose: {you}")
    print(f"com chose: {com}")

    if game == True:
        update_comchoice_label(f"   COM CHOSE : rock")
        update_result_label("******YOU WIN******")
        update_player_info(name, 2)
    elif game == False:
        update_comchoice_label(f"   COM CHOSE : scissors")
        update_result_label("!!!!!!YOU LOSE!!!!!!")
        update_player_info(name, 0)
    elif game == None:
        update_comchoice_label(f"   COM CHOSE : paper")
        update_result_label('''""""""The Game is a tie"""""""''')
        update_player_info(name, 1)


def scissors_button_pressed():
    you = 's'
    print("scissor button pressed")
    randNo = random.randint(1, 3)
    if randNo == 1:
        com = 'r'
    elif randNo == 2:
        com = 'p'
    else:
        com = 's'
    game = gamewin(com, you)
    print(f"you chose: {you}")
    print(f"com chose: {com}")

    if game == True:
        update_comchoice_label(f"   COM CHOSE : paper")
        update_result_label("******YOU WIN******")
        update_player_info(name, 2)
    elif game == False:
        update_comchoice_label(f"   COM CHOSE : rock")
        update_result_label("!!!!!!YOU LOSE!!!!!!")
        update_player_info(name, 0)
    elif game == None:
        update_comchoice_label(f"   COM CHOSE : scissors")
        update_result_label('''""""""The Game is a tie"""""""''')
        update_player_info(name, 1)


def working_leaderboard():
    # Create the main window
    leaderboardwindow = Tk()
    leaderboardwindow.title("Leaderboard")
    leaderboardwindow.geometry("300x300")
    leaderboardwindow.configure(bg="light grey")

    # Create a label for the title
    title_label = Label(leaderboardwindow, text="Leaderboard", fg="red", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    # Query to Execute
    query1 = "SELECT NAME, SCORE FROM gametable ORDER BY SCORE DESC LIMIT 5"

    # Create a Treeview widget
    leaderboard_tree = ttk.Treeview(leaderboardwindow)
    leaderboard_tree["columns"] = ("Name", "Score")

    # Style the Treeview widget
    style = ttk.Style(leaderboard_tree)
    style.theme_use("winnative")
    style.configure("Treeview", rowheight="30", font=("Times", 12), fieldbackground='white', background="white")
    style.configure("leaderboard_tree.heading", font=("Roman", 16, "bold"), fg="red")

    # Assign the width, and anchor to the respective column and heading
    leaderboard_tree.column("#0", width=50, anchor=CENTER)
    leaderboard_tree.column("Name", width=100, anchor=CENTER)
    leaderboard_tree.column("Score", width=100, anchor=CENTER)
    leaderboard_tree.heading("#0", text="Rank", anchor=CENTER)
    leaderboard_tree.heading("Name", text="Name", anchor=CENTER)
    leaderboard_tree.heading("Score", text="Score", anchor=CENTER)
    leaderboard_tree.pack()

    # Create a cursor object to interact with the database
    cursor = rpsdb.cursor()

    # Retrieve data from the database
    cursor.execute(query1)
    leaderboard_data = cursor.fetchall()

    # Insert data into the Treeview
    for i, (Name, Score) in enumerate(leaderboard_data, start=1):
        leaderboard_tree.insert("", "end", text=str(i), values=(Name, Score))

    # Close the database connection
    rpsdb.close()

    # Run the main window loop
    leaderboardwindow.mainloop()


GUI = tkinter.Tk(className='Rock Paper Scissors')
GUI.config(bg="antique White")
GUI.geometry("800x700")
TopLabel = Label(GUI, text="ROCK PAPERS SCISSORS", bg='grey', fg='white', font=("Arial", 28), borderwidth=1,
                 relief="sunken",
                 height=1)
TopLabel.pack(fill="x", padx=10, pady=10)

midLabel = Label(GUI, text="PLAYER                VS                COMPUTER", bg='cyan', fg='blue', font=("Arial", 18),
                 height=5)
midLabel.pack(fill="x", padx=10, pady=10)

# user entry frame starts
userentryframe = Frame(GUI, bg="antique White")

# Label before name which says enter your name
name_label = Label(userentryframe, text="Enter your name :", bg="antique White", fg='black', font=("BOLD", 20),
                   height=4)
name_label.grid(row=0, column=1, sticky="e")

username = StringVar()
userentry = Entry(userentryframe, textvariable=username, width=30, font="20", borderwidth=5, bg="lightblue")
userentry.grid(row=0, column=2, padx=10)
name = userentry.get()

# add top left button for leader board using anchor
leader_board_button = Button(userentryframe, text="LeaderBoard", fg="yellow", bg="black", borderwidth=6, width=10,
                             command=working_leaderboard)
leader_board_button.grid(row=0, column=0, padx=80)


def get_name():
    global name
    name = username.get()
    if name.strip() == "":
        print("No name entered.")
    else:
        print("Name entered:", name)
        # Insert the player's name and score into the database
        update_player_info(name, 0)


submit_button = Button(userentryframe, text="Submit", bg='gray', borderwidth=5, command=get_name)
submit_button.grid(row=0, column=3, padx=10)

userentryframe.pack(padx=30, pady=10)
userentryframe.pack(padx=30, pady=10)
# user entry frame ends


# BUTTON FRAME STARTS
buttonframe = Frame(GUI, bg="antique White")

TopLabel = Label(buttonframe, text="Click on your choice", bg="antique White", fg='black', font=("BOLD", 18),
                 borderwidth=0,
                 relief="sunken",
                 height=2)
TopLabel.grid(row=0, column=2, sticky="ew")

# ROCK BUTTON
rockbutton = Button(buttonframe, bg='gray', text="ROCK", fg='black', width='20', borderwidth=5,
                    command=rock_button_pressed)
rockbutton.grid(row=1, column=1, padx=40)
# PAPER BUTTON
paperbutton = Button(buttonframe, bg='gray', text="PAPERS", fg='black', width='20', borderwidth=5,
                     command=paper_button_pressed)
paperbutton.grid(row=1, column=2, padx=40)
# SCISSORS BUTTON
scissorsbutton = Button(buttonframe, bg='gray', text="SCISSORS", fg='black', width='20', borderwidth=5,
                        command=scissors_button_pressed)
scissorsbutton.grid(row=1, column=3, padx=40)
buttonframe.pack()
# BUTTON FRAME ENDS

# what com chose
comchoiceLabel = Label(GUI, text="", bg="antique White", fg='black', font=("Arial", 12), height=5)
comchoiceLabel.pack(fill="x", padx=10, pady=10)

# result Label
resultLabel = Label(GUI, text="", bg="antique White", fg='red', font=("Arial", 18), height=10)
resultLabel.pack(fill="x", padx=10, pady=10)

GUI.mainloop()
