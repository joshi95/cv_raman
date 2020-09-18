# # Patter 1

#    *
#   * *
#  * * *
# * * * *

# n = int(input())
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print((str(i) + " ") * (i))


# * * * * 
#   * * *
#     * *
#       *

# n = 10
# cur_row = 1
# while cur_row <= n:
#     print(" " * (cur_row - 1), end="")
#     print("*" * (n - cur_row + 1))
#     cur_row+=1

# # n = 4
# # * * * *
# # *     *
# # *     *
# # * * * *



# n = 10
# for row_no in range(1, n + 1):
#     print(" " * (n - row_no), end="")
#     for counter in range(1, row_no + 1):
#         print((str(counter) + " "), end="")
#     print()
    


# Authentication System

# def create_account(user_pass_dict):
#     print("Please enter your desired username: ", end="")
#     username = input()
#     print("Please enter you desired password: ", end="")
#     password = input()
#     user_pass_dict[username] = password
#     return user_pass_dict

def get_username_password():
    print("Please enter your desired username: ", end="")
    username = input()
    print("Please enter you desired password: ", end="")
    password = input()
    return username, password

def signup(username_to_password_dict):
    username, password = get_username_password()
    if username in username_to_password_dict:
        print("error: username already taken")
        return
    username_to_password_dict[username] = password
    print("the dictionary is ", username_to_password_dict)

def login(username_to_password_dict):
    username, password = get_username_password()
    if username not in username_to_password_dict:
        print("error: username doesn't exit")
        return
    expected_password = username_to_password_dict[username]
    if password == expected_password:
        print("successfull login")
    else:
        print("invalid login")

def show_all_accounts(username_to_pass_dict):
    print("All users are ", username_to_pass_dict.keys())

print("Authentication System")
username_to_password_dict = dict()
while True:
    print("1. Press to create an account")
    print("2. Press to login")
    print("3. press to show all the users")
    print("4. press to exit")

    x = int(input())

    if x == 4:
        print("Thank You ! Come Again :)")
        break
    elif x == 1:
        signup()
    elif x == 2:
        login()
    elif x == 3:
        show_all_accounts(username_to_password_dict)
    else:
        print("Hey invalid input. Please Try Again!")
