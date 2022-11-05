import random
import string
import hashlib
import requests


class Passeo:
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
                if uppercase:
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

        def strengthcheck(password):
            sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
            first5, tail = sha1password[:5], sha1password[5:]
            response = requests.get('https://api.pwnedpasswords.com/range/' + first5)
            y = tail in response.text
            length = len(password)
            StrengthCheckQuiz = {
            }
            if y == True:
                StrengthCheckQuiz['Pwned'] = 'PASS: password has been pwned, please change it.'
            if y == False:
                StrengthCheckQuiz['Pwned'] = 'PASS: Your password has not been pwned, you are safe.'
            if y == None:
                StrengthCheckQuiz['Pwned'] = 'FAIL: An error has occurred, please try again.'
            if length < 8:
                StrengthCheckQuiz['Length'] = 'FAIL: Your password is too short, it is recommended to make it longer.'

            if length > 8 and length < 16:
                StrengthCheckQuiz['Length'] = 'PASS: Your password is long enough! It could be longer, but is great.'

            if length > 16:
                StrengthCheckQuiz['Length'] = 'PASS: Your password is very long, good job!'

            return str(StrengthCheckQuiz['Pwned']) + '\n' + str(StrengthCheckQuiz['Length'] + '\n' + 'The Passeo password strength test has ended. Any questions/bugs? Raise a issue on https://github.com/ArjunSharda/Passeo/issue.')
        self.strengthcheck = strengthcheck
