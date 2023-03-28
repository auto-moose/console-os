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
    
#Writes acc_info dict to json file
def save_acc_info(info):
    with open("acc_info.json", "w") as file:
        json.dump(info, file, indent=4)

#Loads acc_info dict with json file
def load_acc_info():
    with open("acc_info.json", "r") as file:
        info = json.load(file)
    return info

def change_acc_info(key, value):
    acc_info[key] = value
    save_acc_info(acc_info)

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

    change_acc_info("acc_created", True)
    change_acc_info("username", username)
    change_acc_info("password", password)
    print_line(15)
    startup()

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

                        change_acc_info("password", password)
                        continue
                    
          
                trys += 1                 
                print("\nIncorrect password, please try again: ")
                

    else:
        create_account()

def main():
    while True:
        input()
acc_info = load_acc_info()
startup()
