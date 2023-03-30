import json
import random
import time

def print_line(lines=1, text=""):
    for i in range(lines):
        print(text)

def print_chars(text, duration=0, wait=0, newline=True):

    for char in text:
        print(char, end='')
        time.sleep(duration/len(text))
    time.sleep(wait)

    if newline:
        print("")
    
#           Note:
# This currently only supports one user.
# Later on data will be stored for multiple
# users inside of objects derived from the
# base User class, however this funcionality
# has not been added yet

#Writes dict to json file
def save_json(file, info):
    with open(file, "w") as f:
        json.dump(info, f, indent=4)

#Loads dict with json file
def load_json(file="acc_info.json"):
    with open(file, "r") as f:
        info = json.load(f)
    return info

#Changes value in dict and automatically saves it to json
def change_dict(file, json_dict, key, value):
    json_dict[key] = value
    save_json(file, json_dict)

#Called when account is deleted or not stored in json
def create_account():
    print_chars("There is no account created on this device", 1, 0.5)
    print_chars("Please create a new account", 0.5, 0.5)

    while True:
        print_chars("\nEnter username: ", 0.5, 0, False)
        username = input()
        continued = input("\nDo you want to continue as " + username + "? (y/n): ")

        if continued.lower() == "y" or continued.lower() == "yes":
            break

    while True:
        print_chars("\nEnter a password for \""+username+"\": ", 0.5, 0, False)
        password = input()
        print_chars("\nPlease confirm your password: ", 0.5, 0, False)
        confirm_password = input()
        if confirm_password != password:
            print("Error: Confirmed password does not match, please try again")
            continue
        continued = input("\nAre you okay with this password? (y/n): ")

        if continued.lower() == "y" or continued.lower() == "yes":
            break

    change_dict("acc_info.json", acc_info, acc_created, True)
    change_dict("acc_info.json", acc_info, "username", username)
    change_dict("acc_info.json", acc_info, "password", password)
    print_line(15)
    startup()

#Called at start
def startup():
    if acc_info["acc_created"]:
        print_chars("Starting", 0.5, 0.5)
        print_line(10, "*")
        print_chars("Hello, " + acc_info["username"] + ".", 0.1, 3)
        
        trys = 1
        while True:
            print_chars("\nPlease enter your password: ", 0.5, 0, False)
            entered_password = input()

            if entered_password == acc_info["password"]:
                print_chars("\nLogging in", 1, 0, False)
                print_chars("...", 3, 3)
                print_line(10, "*")
                main()
            else:
                #If user takes too many guesses they will be able to reset their password
                if trys >= 3:
                    print("\nIncorrect password")
                    reset = input("It seems you have forgotten your password, would you like to reset it? (y/n): ")

                    if reset.lower() == "y" or reset.lower() == "yes":

                        while True:
                            username = acc_info["username"]

                            print_chars("\nEnter a password for \""+username+"\": ", 0.5, 0, False)
                            password = input()

                            print_chars("\nPlease confirm your password: ", 0.5, 0, False)
                            confirm_password = input()
                            
                            if confirm_password != password:
                                print("Error: Confirmed password does not match, please try again")
                                continue

                            continued = input("\nAre you okay with this password? (y/n): ")
                            if continued.lower() == "y" or continued.lower() == "yes":
                                break

                        change_dict("acc_info.json", acc_info, "password", password)
                        continue
                    
          
                trys += 1                 
                print("\nIncorrect password, please try again: ")
                

    else:
        create_account()

#Simple calculator - can only add, subtract, multiply or divide 2 numbers.
def calculator():
    while True:
        while True:
            print_chars("\nWhat would you like to do? (add/subtract/multiply/divide): ", 0.5, 0, False)
            operation = input()

            if operation.lower() == "add" or operation.lower() == "+":
                operation = "+"
            elif operation.lower() == "subtract" or operation.lower() == "-" or operation.lower() == "minus":
                operation = "-"
            elif operation.lower() == "multiply" or operation.lower() == "x" or operation.lower() == "times" or operation.lower() == "*":
                operation = "*"
            elif operation.lower() == "divide" or operation.lower() == "/":
                operation = "/"
            else:
                print("\nError, invalid command. Please try again.")
                continue
            break

        while True:
            print_chars("\nEnter your first number: ", 0.5, 0, False)
            num1 = input()

            try:
                num1 = int(num1)
                break
            except:
                print("Error - your value must be a number")

        while True:
            print_chars("\nEnter your second number: ", 0.5, 0, False)
            num2 = input()

            try:
                num2 = int(num2)
                break
            except:
                print("\nError - your value must be a number")

        print_line()

        if operation == "+":
            print(num1 + num2)
        elif operation == "-":
            print(num1 - num2)
        elif operation == "*":
            print(num1 * num2)
        else:
            print(num1 / num2)

        print_chars("\nPress q to quit or any other key to continue: ", 0.5, 0, False)
        exit_input = input()

        if exit_input.lower() == "q" or exit_input.lower() == "quit":
            break

def tic_tac_toe():

    points = tic_tac_toe_info["score"]

    line = "|---|---|---|"

    while True:
        row1 = ['1', '2', '3']
        row2 = ['4', '5', '6']
        row3 = ['7', '8', '9']

        print("""

    |---|---|---|
    | 1 | 2 | 3 |
    |---|---|---|
    | 4 | 5 | 6 |
    |---|---|---|
    | 7 | 8 | 9 |
    |---|---|---|

    """)

        p1_turn = True
        p2_turn = False

        for i in range(9):

            if p1_turn:
                while True:
                    p1_choice = int(input("\nPlayer 1 enter your position (1 - 9) "))

                    if p1_choice < 4:
                        
                        if row1[p1_choice - 1] == "X" or row1[p1_choice - 1] == "O":
                            print("\nSorry that square has already been chosen. Please choose another one.")
                        else:
                            row1[p1_choice - 1] = "X"
                            break
                        
                    elif p1_choice < 7:
                        if row2[p1_choice - 4] == "X" or row2[p1_choice - 4] == "O":
                            print("\nSorry that square has already been chosen. Please choose another one.")
                        else:
                            row2[p1_choice - 4] = "X"
                            break
                    else:
                        if row3[p1_choice - 7] == "X" or row3[p1_choice - 7] == "O":
                            print("\nSorry that square has already been chosen. Please choose another one.")
                        else:
                            row3[p1_choice - 7] = "X"
                            break
            else:
                while True:
                    p2_choice = int(input("\nPlayer 2 enter your position (1 - 9) "))

                    if p2_choice < 4:
                        
                        if row1[p2_choice - 1] == "X" or row1[p2_choice - 1] == "O":
                            print("\nSorry that square has already been chosen. Please choose another one.")
                        else:
                            row1[p2_choice - 1] = "O"
                            break
                        
                    elif p2_choice < 7:
                        if row2[p2_choice - 4] == "X" or row2[p2_choice - 4] == "O":
                            print("\nSorry that square has already been chosen. Please choose another one.")
                        else:
                            row2[p2_choice - 4] = "O"
                            break
                    else:
                        if row3[p2_choice - 7] == "X" or row3[p2_choice - 7] == "O":
                            print("\nSorry that square has already been chosen. Please choose another one.")
                        else:
                            row3[p2_choice - 7] = "O"
                            break




            print(line)
            print("| " + row1[0] + " |" + " " + row1[1] + " |" + " " + row1[2] + " |")
            print(line)
            print("| " + row2[0] + " |" + " " + row2[1] + " |" + " " + row2[2] + " |")
            print(line)
            print("| " + row3[0] + " |" + " " + row3[1] + " |" + " " + row3[2] + " |")
            print(line)


            if row1[0] + row1[1] + row1[2] == "XXX" or row1[0] + row1[1] + row1[2] == "OOO":
                if p1_turn:
                    print("P1 WINS!!")
                    points[0] += 1
                    break
                else:
                    print("P2 WINS!!")
                    points[1] += 1
                    break
            if row2[0] + row2[1] + row2[2] == "XXX" or row2[0] + row2[1] + row2[2] == "OOO":
                if p1_turn:
                    print("P1 WINS!!")
                    points[0] += 1
                    break
                else:
                    print("P2 WINS!!")
                    points[1] += 1
                    break
            if row3[0] + row3[1] + row3[2] == "XXX" or row3[0] + row3[1] + row3[2] == "OOO":
                if p1_turn:
                    print("P1 WINS!!")
                    points[0] += 1
                    break
                else:
                    print("P2 WINS!!")
                    points[1] += 1
                    break
            if row1[0] + row2[0] + row3[0] == "XXX" or row1[0] + row2[0] + row3[0] == "OOO":
                if p1_turn:
                    print("P1 WINS!!")
                    points[0] += 1
                    break
                else:
                    print("P2 WINS!!")
                    points[1] += 1
                    break
            if row1[1] + row2[1] + row3[1] == "XXX" or row1[1] + row2[1] + row3[1] == "OOO":
                if p1_turn:
                    print("P1 WINS!!")
                    points[0] += 1
                    break
                else:
                    print("P2 WINS!!")
                    points[1] += 1
                    break
            if row1[2] + row2[2] + row3[2] == "XXX" or row1[2] + row2[2] + row3[2] == "OOO":
                if p1_turn:
                    print("P1 WINS!!")
                    points[0] += 1
                    break
                else:
                    print("P2 WINS!!")
                    points[1] += 1
                    break
            if row1[0] + row2[1] + row3[2] == "XXX" or row1[0] + row2[1] + row3[2] == "OOO":
                if p1_turn:
                    print("P1 WINS!!")
                    points[0] += 1
                    break
                else:
                    print("P2 WINS!!")
                    points[1] += 1
                    break
            if row1[2] + row2[1] + row3[0] == "XXX" or row1[2] + row2[1] + row3[0] == "OOO":
                if p1_turn:
                    print("P1 WINS!!")
                    points[0] += 1
                    break
                else:
                    print("P2 WINS!!")
                    points[1] += 1
                    break



            if p1_turn:
                p1_turn = False
                p2_turn = True
            else:
                p2_turn = False
                p1_turn = True

        change_dict("tic_tac_toe.json", tic_tac_toe_info, "score", points)
        print(str(points[0]) + "-" + str(points[1]))

        print_chars("\nPress q to quit or any other key to continue: ", 0.5, 0, False)
        exit_input = input()

        if exit_input.lower() == "q" or exit_input.lower() == "quit":
            break

    


#This is where the user can acess different apps inside the os
def main():
    while True:
        print_chars("\nWhat would you like to do: ", 0.5, 0, False)
        command = input()

        if command.lower() == "calc" or command.lower() == "calculator":
            calculator()
        if command.lower() == "tic-tac-toe" or command.lower() == "tictactoe":
            tic_tac_toe()

#Copys json file to main dictionary which will be acessed throughout the script
acc_info = load_json()
tic_tac_toe_info = load_json("tic_tac_toe.json")

startup()
