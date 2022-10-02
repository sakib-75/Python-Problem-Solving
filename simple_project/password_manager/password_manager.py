from cryptography.fernet import Fernet


def view():
    print('\nView existing password')
    with open('passwords.txt', 'r') as file:
        for i, line in enumerate(file.readlines()):
            data = line.rstrip()
            key, user, passw = data.split('|')
            fernet = Fernet(key.encode())
            decrypt_user = fernet.decrypt(user.encode()).decode()
            decrypt_pass = fernet.decrypt(passw.encode()).decode()
            print(i + 1, 'Username:', decrypt_user, ',', 'Password:', decrypt_pass)


def add():
    username = input('Username: ')
    password = input('Password: ')
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypt_username = fernet.encrypt(username.encode()).decode()
    encrypt_password = fernet.encrypt(password.encode()).decode()
    with open('passwords.txt', 'a') as file:
        file.write(key.decode() + '|' + encrypt_username + '|' + encrypt_password + '\n')


while True:
    print("\n")
    print("Enter v for view")
    print("Enter a for add")
    print("Enter q for quit")

    option = input('Enter your option: ').lower()

    if option == 'q':
        break
    elif option == 'v':
        view()
    elif option == 'a':
        add()
    else:
        print('Invalid option')
