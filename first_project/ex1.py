


#PYTHON PROJECT



# user information
user_list = {}

def add_user(name, user_info):
    user_list[name] = user_info

def view_user():
    for name, info in user_list.items():
        print(f"Name: {name}")
        print(f"Phone: {info('phone')}")
        print(f"Email: {info('email')}")
        print()
# while adding a user FUNCTION

while True:
    action = input("Do you want to add a user or view the inforamtion of user? (add a user/view information/exit)")
    if action == "add a user":
        name = input("Enter the name of user: ")
        phone =  input("Enter the phone number of the user: ")
        email = input("Enter the email of the user: ")
        work = print("We are creating a new user for you. ")
        left = exit("Please wait! It may take a few moments......")
        user_info = {"phone": {phone}, "email": {email}}
        add_user(name, user_info)

# view information FUNCTION
    if action == "view information":
        name = print("This computer has only one user. Which is mrjanjua@Mubashir.")
        phone = print("Their phone No: 03338905344")
        email = print("Their email address: iammansoor9906@gmail.com")
        left = exit("Try it again to add a user to the computer.")

# exit FUNCTION
    if action == "exit":
        exit = exit("Thank you for using this software.")
    else:
        exit("Please try agian later!")
        