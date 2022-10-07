from cryptography.fernet import Fernet


# encode() = string ---> byte
# decode() = byte ---> string


def view_password():
    with open('passwords.txt', 'r') as file:
        lines = file.readlines()
        if len(lines) > 0:
            print('\n...View existing password...')
            for i, line in enumerate(lines):
                data = line.rstrip()
                key, user, passw = data.split('|')
                fernet = Fernet(key.encode())
                decrypt_user = fernet.decrypt(user.encode()).decode()
                decrypt_pass = fernet.decrypt(passw.encode()).decode()
                print(i + 1, 'Username:', decrypt_user, ',', 'Password:', decrypt_pass)
        else:
            print("No password available!")


def add_password():
    username = input('Username: ')
    password = input('Password: ')
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypt_username = fernet.encrypt(username.encode()).decode()
    encrypt_password = fernet.encrypt(password.encode()).decode()
    with open('passwords.txt', 'a') as file:
        file.write(key.decode() + '|' + encrypt_username + '|' + encrypt_password + '\n')
    print('Password added!')


def remove_all_password():
    with open('passwords.txt', 'r+') as file:
        file.truncate(0)

    # file = open('passwords.txt', 'r+')
    # file.truncate(0)
    # file.close()

    print('All password removed!')


while True:
    print('\n')
    print('...Login Page...')
    print('[1] Login')
    print('[2] Register')
    print('[3] Quit')
    option = input('Enter your option: ')

    if option == '1':
        is_login = False
        login_username = input('type your username to login:')
        login_password = input('type your password to login:')

        with open('login.txt', 'r') as file:
            lines = file.readlines()
            if len(lines) > 0:
                for line in lines:
                    data = line.strip()
                    key, username, password = data.split(',')
                    fernet = Fernet(key.encode())
                    decrypt_user = fernet.decrypt(username.encode()).decode()
                    decrypt_pass = fernet.decrypt(password.encode()).decode()
                    if login_username == decrypt_user and login_password == decrypt_pass:
                        is_login = True
                        break

                if is_login:
                    print('Login success!')
                else:
                    print('Invalid username or password!')
            else:
                print('No registered user available!')

        while is_login:
            print("\n")
            print('...Password Page...')
            print("Enter v for view password")
            print("Enter a for add password")
            print("Enter r for remove all password")
            print("Enter q for quit")

            option = input('Enter your option: ').lower()

            if option == 'q':
                break
            elif option == 'v':
                view_password()
            elif option == 'a':
                add_password()
            elif option == 'r':
                remove_all_password()
            else:
                print('Invalid option')

    elif option == '2':
        username = input('Username for register: ')
        password = input('Password for register: ')
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encrypt_username = fernet.encrypt(username.encode()).decode()
        encrypt_password = fernet.encrypt(password.encode()).decode()
        with open('login.txt', 'a') as file:
            file.write(key.decode() + ',' + encrypt_username + ',' + encrypt_password + '\n')
        print('User added!')

    elif option == '3':
        break

    else:
        print('Invalid option')
