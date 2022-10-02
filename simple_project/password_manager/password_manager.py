from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)


def view():
    print('\nView existing password')
    with open('passwords.txt', 'r') as file:
        for i, line in enumerate(file.readlines()):
            data = line.rstrip()
            key, user, passw = data.split('|')
            fernet = Fernet(key.encode())
            decrypt_pass = fernet.decrypt(passw.encode()).decode()
            print(i + 1, 'Username: ', user, ',', 'Password: ', decrypt_pass)


def add():
    username = input('Username: ')
    password = input('Password: ')
    encrypt_pass = fernet.encrypt(password.encode()).decode()

    with open('passwords.txt', 'a') as file:
        file.write(key.decode() + '|' + username + '|' + encrypt_pass + '\n')


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
