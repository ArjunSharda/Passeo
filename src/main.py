import random
import string


class Passeo():
    def __init__(self):

        def generate(length, numbers=False, symbols=False, uppercase=False, lowercase=False, space=False, save=False):
            password = ''
            if numbers:
                password += string.digits
            if symbols:
                password += string.punctuation
            if uppercase:
                password += string.ascii_uppercase
            if lowercase:
                if uppercase == True:
                    raise ValueError('Uppercase and lowercase are both true, please make one of them false.')
                password += string.ascii_lowercase
            if space:
                password += ' '
            PasseoPassword = ''.join(random.sample(password, length))
            if save:
                with open('passeo_passwords.txt', 'a') as file:
                    file.write(PasseoPassword + '\n')
            return PasseoPassword
        self.generate = generate
