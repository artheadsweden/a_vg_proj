'''
Password Strength Checker
-------------------------------------------------------------
'''


import string
import getpass

def check_password_strength2():
    password = getpass.getpass('Enter the password: ')
    result = {
        'lower_count': sum(1 for char in password if char in string.ascii_lowercase),
        'upper_count': sum(1 for char in password if char in string.ascii_uppercase),
        'num_count': sum(1 for char in password if char in string.digits),
        'wspace_count': sum(1 for char in password if char == ' '),
        'special_count': sum(1 for char in password if char not in string.ascii_letters + string.digits + ' '),
    }
    strength = sum(1 for key, value in result.items() if value >= 1)
    if strength == 1:
        remarks = ('That\'s a very bad password.'
           ' Change it as soon as possible.')
    elif strength == 2:
        remarks = ('That\'s a weak password.'
           ' You should consider using a tougher password.')
    elif strength == 3:
        remarks = 'Your password is okay, but it can be improved.'
    elif strength == 4:
        remarks = ('Your password is hard to guess.'
           ' But you could make it even more secure.')
    elif strength == 5:
        remarks = ('Now that\'s one hell of a strong password!!!'
           ' Hackers don\'t have a chance guessing that password!')

    print('Your password has:-')
    print(f'{result["lower_count"]} lowercase letters')
    print(f'{result["upper_count"]} uppercase letters')
    print(f'{result["num_count"]} digits')
    print(f'{result["wspace_count"]} whitespaces')
    print(f'{result["special_count"]} special characters')
    print(f'Password Score: {strength / 5}')
    print(f'Remarks: {remarks}')


def check_pwd(another_pw=False):
    if another_pw:
        choice = input(
            'Do you want to check another password\'s strength (y/n) : ')
    else:
        choice = input(
            'Do you want to check your password\'s strength (y/n) : ')

    while True:
        if choice.lower() not in 'yn':
            print('Invalid input...please try again. \n')
        else:
            return choice.lower() == 'y'


if __name__ == '__main__':
   print('===== Welcome to Password Strength Checker =====')
   check_pw = check_pwd()
   while check_pw:
       check_password_strength2()
       check_pw = check_pwd(True)