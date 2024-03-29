import hashlib
import secrets
import string
import bcrypt

import requests
from aenum import Enum
from cryptography.fernet import Fernet


class passeo(Enum):

    def generate(self, length, numbers=False, symbols=False, uppercase=False, lowercase=False, space=False, save=False):
        password = ''

        if numbers is True:
            password += secrets.choice(string.digits)
        if symbols is True:
            password += secrets.choice(string.punctuation)
        if lowercase and uppercase == True:
            raise ValueError('Uppercase and lowercase are both true, please make one of them false.')
        if uppercase is True:
            password += secrets.choice(string.ascii_uppercase)
        if lowercase is True:
            password += secrets.choice(string.ascii_lowercase)
        if space is True:
            password += ' '
        PasseoPassword = ''.join(secrets.choice(password) for i in range(length))
        if save is True:
            with open('passeo_passwords.txt', 'a') as file:
                file.write(PasseoPassword + '\n')
        return PasseoPassword

    def strengthcheck(self, password):
        sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        first5, tail = sha1password[: 5], sha1password[5:]
        response = requests.get('https://api.pwnedpasswords.com/range/' + first5)
        y = tail in response.text
        length = len(password)
        StrengthCheckQuiz = {
            'Pwned': '',
            'Length': '',
            'Case': '',
        }
        if y == True:
            StrengthCheckQuiz['Pwned'] = '1/3: PASS: password has been pwned, please change it.'
        elif y == False:
            StrengthCheckQuiz['Pwned'] = '1/3: PASS: Your password has not been pwned, you are safe.'
        elif y == None:
            StrengthCheckQuiz['Pwned'] = '1/3: FAIL: An error has occurred, please try again.'
        if length < 8:
            StrengthCheckQuiz['Length'] = '2/3: FAIL: Your password is too short, it is recommended to make it longer.'
        elif length >= 8 and length <= 16:
            StrengthCheckQuiz['Length'] = '2/3: PASS: Your password is long enough! It could be longer, but is great.'
        elif length > 16:
            StrengthCheckQuiz['Length'] = '2/3: PASS: Your password is very long, good job!'
        elif length == None:
            StrengthCheckQuiz['Length'] = '2/3: FAIL: An error has occurred, please try again.'
        if password.lower():
            StrengthCheckQuiz[
                'Case'] = '3/3: FAIL: Your password has lowercase letters, but not uppercase letters, it is recommended to add uppercase letters.'
        elif password.upper():
            StrengthCheckQuiz[
                'Case'] = '3/3: FAIL: Your password has uppercase letters, however it is also recommended to add lowercase letters.'
        elif password.lower() and password.upper():
            StrengthCheckQuiz['Case'] = '3/3: PASS: Your password has both uppercase and lowercase letters, good job!'
        elif password == None:
            StrengthCheckQuiz['Case'] = '3/3: FAIL: An error has occurred, please try again.'
        return str(StrengthCheckQuiz['Pwned']) + '\n' + str(StrengthCheckQuiz['Length']) + '\n' + str(
            StrengthCheckQuiz['Case'])

    def quickgenerate(length=int, save=False, bulk=1):
        PASSEO_QUICKGEN_PASSWORD = ''.join(
            secrets.choice(
                string.ascii_letters + string.digits + string.ascii_uppercase + string.punctuation + string.hexdigits + string.octdigits + string.whitespace)
            for i in range(length))
        if save:
            with open('passeo_quickgen_passwords.txt', 'a') as file:
                file.write(PASSEO_QUICKGEN_PASSWORD + '\n')
        if bulk > 1:
            with open('passeo_quickgen_bulk_passwords.txt', 'a') as f:
                for i in range(bulk):
                    f.write(''.join(
                        passeo().generate(length, numbers=True, symbols=True, uppercase=False,
                                          lowercase=False) + secrets.choice(string.ascii_lowercase) + secrets.choice(
                            string.ascii_uppercase) + '\n')),

        return PASSEO_QUICKGEN_PASSWORD

    def encrypt(data):
        key = Fernet.generate_key()
        f = Fernet(key)
        encrypted_data = f.encode(data.encrypt())
        return encrypted_data, key

    def decrypt(encrypted_data):
        key = encrypted_data[1]
        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data[0]).decrypt()
        return decrypted_data
