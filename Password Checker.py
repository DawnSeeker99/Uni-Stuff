banned_passwords = ["huddersfield", "justinbieber", "cheese", "canalside", ]

username = input("Please enter your student ID: ")
password = input("Please enter your current password: ")
banned_passwords.append(username)
banned_passwords.append(password)

while True:
    new_password = input("Please enter your new password: ")
    if 6 <= len(new_password) <= 12 and new_password not in banned_passwords:
        comfirm_new_password = input("Please confirm your new password: ")
        if new_password == comfirm_new_password:
            print('Your password has been changed.')
            break
        else:
            print('Passwords do not match.')
    elif new_password in banned_passwords:
        print("This is a forbidden password, please enter a stronger password.")
    else:
        print("Your password must be between 6 and 12 characters.")
