# -------------------------------
# Authentication Program (File-Based)
# -------------------------------

import os

def load_users():
    users = {}
    with open("users.txt", "r") as file:
        for line in file:
            if ":" in line:
                username, password = line.strip().split(":", 1)
                users[username] = password
    return users


def open_downloads_folder():
    user_home = os.path.expanduser("~")
    
    # Change "Downloads" to "Desktop" if you specifically want the Desktop folder
    target_folder = "Downloads" 
    
    standard_path = os.path.join(user_home, target_folder)
    onedrive_path = os.path.join(user_home, "OneDrive", target_folder)

    if os.path.exists(standard_path):
        os.startfile(standard_path)
    elif os.path.exists(onedrive_path):
        os.startfile(onedrive_path)
    else:
        print(f"Error: Could not find the {target_folder} folder.")


def authenticate():
    print("User Authentication Required")

    users = load_users()

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in users and users[username] == password:
        print("\n Authentication Successful")
        print(" Access Granted")
        print(" Opening Downloads Folder...")
        open_downloads_folder()
    else:
        print("\n Authentication Failed")
        print(" Access Denied")


# -------------------------------
# MAIN
# -------------------------------
authenticate()