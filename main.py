#3
import random
class PasswordGenerator:
    def __init__(self, lenth, symbols):
        self.lenth = lenth
        self.symbols = symbols
    def genarate_password(self):
        password = ''
        for i in range(self.lenth):
            password += random.choice(self.symbols)
        return password
generator = PasswordGenerator(10, 'qwertyQWERTY1234!@#$%^_-.')
for i in range(3):
    print(f"Ваш пароль: {generator.genarate_password()}")